use std::{
    fs::{self, File},
    io::Write,
    path::{Path, PathBuf},
    process::Command,
    thread,
    time::{Duration, Instant, SystemTime, UNIX_EPOCH},
};

use log::{debug, error, info, warn};

const INVOCATION_INTERVAL: Duration = Duration::from_secs(10);

const MODEL: &str = "opencode/deepseek-v4-flash-free";
const TRIAGE_DIRECTORY: &str = "queue/00-triage";
const DOING_DIRECTORY: &str = "queue/01-doing";
const DONE_DIRECTORY: &str = "queue/02-done";
const BACKLOG_DIRECTORY: &str = "queue/03-backlog";

/// Removes terminal control sequences that do not belong in a plain-text log file.
fn strip_ansi(input: &[u8]) -> Vec<u8> {
    let mut output = Vec::with_capacity(input.len());
    let mut index = 0;

    while index < input.len() {
        if input[index..].starts_with(b"\x1b[") {
            index += 2;
            while index < input.len() && !(0x40..=0x7e).contains(&input[index]) {
                index += 1;
            }
            index += usize::from(index < input.len());
        } else {
            output.push(input[index]);
            index += 1;
        }
    }

    output
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

/// Returns the next supported prompt file in a stable order.
fn next_prompt() -> std::io::Result<Option<PathBuf>> {
    let entries = fs::read_dir(TRIAGE_DIRECTORY)?
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.is_file() && !is_hidden_file(path))
        .collect::<Vec<_>>();

    let (mut prompts, invalid_files): (Vec<_>, Vec<_>) =
        entries.into_iter().partition(|path| is_prompt_file(path));

    if !invalid_files.is_empty() {
        warn!(
            "Found {} invalid files in {TRIAGE_DIRECTORY}",
            invalid_files.len()
        );
        for path in invalid_files {
            debug!("Invalid prompt file: {}", path.display());
        }
    }

    prompts.sort();
    Ok(prompts.into_iter().next())
}

fn is_hidden_file(path: &Path) -> bool {
    path.file_name()
        .and_then(|filename| filename.to_str())
        .is_some_and(|filename| filename.starts_with('.'))
}

fn is_prompt_file(path: &Path) -> bool {
    matches!(
        path.extension().and_then(|extension| extension.to_str()),
        Some("md" | "txt")
    )
}

/// Runs OpenCode with a prompt, saving the prompt and output to a timestamped log file.
fn invoke_opencode(prompt: &str, prompt_path: &Path) {
    let timestamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .expect("system clock is before the Unix epoch")
        .as_millis();

    let log_path = format!("logs/{timestamp}.log");

    info!(
        "Starting OpenCode session for {}; writing output to {log_path}",
        prompt_path.display()
    );

    let mut log_file = File::create(&log_path).expect("failed to create OpenCode log file");
    writeln!(
        log_file,
        "Input prompt ({}):\n{prompt}\n\nOutput:",
        prompt_path.display()
    )
    .expect("failed to write OpenCode log header");

    match Command::new("opencode")
        .args(["run", "--model", MODEL, prompt])
        .output()
    {
        Ok(output) => {
            log_file
                .write_all(&strip_ansi(&output.stdout))
                .expect("failed to write OpenCode stdout to log");
            log_file
                .write_all(&strip_ansi(&output.stderr))
                .expect("failed to write OpenCode stderr to log");
            info!("OpenCode exited with {}", output.status);
        }
        Err(error) => {
            writeln!(log_file, "Failed to start OpenCode: {error}")
                .expect("failed to write OpenCode startup error to log");
            error!("Failed to start OpenCode: {error}");
        }
    }
}

/// Processes the next prompt in triage, then records it in done.
fn process_next_prompt() {
    let Some(triage_path) = next_prompt().expect("failed to read the prompt queue") else {
        return;
    };
    let filename = triage_path
        .file_name()
        .expect("prompt path does not have a filename");

    let prompt = match fs::read_to_string(&triage_path) {
        Ok(prompt) => prompt,
        Err(error) => {
            error!("Could not read {}: {error}", triage_path.display());
            return;
        }
    };

    info!("Processing {}", triage_path.display());
    invoke_opencode(&prompt, &triage_path);

    let done_path = Path::new(DONE_DIRECTORY).join(filename);
    if let Err(error) = fs::rename(&triage_path, &done_path) {
        error!(
            "OpenCode finished, but could not move {} to {}: {error}",
            triage_path.display(),
            done_path.display()
        );
        return;
    }

    info!(
        "Completed {}; moved it to {}",
        filename.to_string_lossy(),
        done_path.display()
    );
}

#[cfg(test)]
mod tests {
    use super::{is_hidden_file, is_prompt_file, strip_ansi};
    use std::path::Path;

    #[test]
    fn removes_ansi_sequences_from_output() {
        assert_eq!(
            strip_ansi(b"hello\n\x1b[0m\n> build\n"),
            b"hello\n\n> build\n"
        );
    }

    #[test]
    fn accepts_only_markdown_and_text_prompts() {
        assert!(is_prompt_file(Path::new("prompt.md")));
        assert!(is_prompt_file(Path::new("prompt.txt")));
        assert!(!is_prompt_file(Path::new("prompt.json")));
    }

    #[test]
    fn ignores_hidden_files() {
        assert!(is_hidden_file(Path::new(".gitkeep")));
        assert!(is_hidden_file(Path::new(".draft.md")));
        assert!(!is_hidden_file(Path::new("prompt.md")));
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

/// Repeatedly runs OpenCode, enforcing the configured minimum invocation interval.
fn main() {
    fs::create_dir_all("logs").expect("failed to create logs directory");
    fs::create_dir_all(TRIAGE_DIRECTORY).expect("failed to create triage queue directory");
    fs::create_dir_all(DOING_DIRECTORY).expect("failed to create doing queue directory");
    fs::create_dir_all(DONE_DIRECTORY).expect("failed to create done queue directory");
    fs::create_dir_all(BACKLOG_DIRECTORY).expect("failed to create backlog queue directory");

    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("info"))
        .target(env_logger::Target::Stdout)
        .init();

    println!(
        "Prompt queue is running. Add .txt or .md prompt files to {TRIAGE_DIRECTORY}.\n\
         Prompts in triage are processed, then moved to {DONE_DIRECTORY}.\n\
         {DOING_DIRECTORY} and {BACKLOG_DIRECTORY} are not processed."
    );

    let mut loop_number = 0_u64;

    loop {
        loop_number += 1;
        info!("Starting loop {loop_number}");
        let started_at = Instant::now();
        process_next_prompt();
        info!("Completed loop {loop_number}");

        if let Some(remaining) = INVOCATION_INTERVAL.checked_sub(started_at.elapsed()) {
            thread::sleep(remaining);
        }
    }
}
