use std::{
    fs::{self, File},
    io::Write,
    process::Command,
    thread,
    time::{Duration, Instant, SystemTime, UNIX_EPOCH},
};

use log::{error, info};

const INVOCATION_INTERVAL: Duration = Duration::from_secs(10);

const PROMPT: &str = "respond hello";
const MODEL: &str = "opencode/deepseek-v4-flash-free";

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

/// Runs OpenCode with the configured prompt and model, saving its output to a timestamped log file.
fn invoke_opencode() {
    let timestamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .expect("system clock is before the Unix epoch")
        .as_millis();

    let log_path = format!("logs/{timestamp}.log");

    info!("Invoking OpenCode at {timestamp}; writing output to {log_path}");

    let mut log_file = File::create(&log_path).expect("failed to create OpenCode log file");
    writeln!(log_file, "Input prompt:\n{PROMPT}\n\nOutput:")
        .expect("failed to write OpenCode log header");

    match Command::new("opencode")
        .args(["run", "--model", MODEL, PROMPT])
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

#[cfg(test)]
mod tests {
    use super::strip_ansi;

    #[test]
    fn removes_ansi_sequences_from_output() {
        assert_eq!(
            strip_ansi(b"hello\n\x1b[0m\n> build\n"),
            b"hello\n\n> build\n"
        );
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

/// Repeatedly runs OpenCode, enforcing the configured minimum invocation interval.
fn main() {
    fs::create_dir_all("logs").expect("failed to create logs directory");

    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("info"))
        .target(env_logger::Target::Stdout)
        .init();

    loop {
        let started_at = Instant::now();
        invoke_opencode();

        if let Some(remaining) = INVOCATION_INTERVAL.checked_sub(started_at.elapsed()) {
            thread::sleep(remaining);
        }
    }
}
