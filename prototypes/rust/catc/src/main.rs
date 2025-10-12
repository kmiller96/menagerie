use std::{env, fs};

// ----------------- //
// -- Subroutines -- //
// ----------------- //

/// Parse command line arguments, returning a tuple of (filepath,)
fn parse_args() -> (String,) {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: catc <filepath>");
        std::process::exit(1);
    }

    let filepath = args[1].clone();
    (filepath,)
}

/// Read the file at the given filepath
fn read_file(filepath: String) -> String {
    match fs::read_to_string(&filepath) {
        Ok(content) => content,
        Err(e) => {
            eprintln!("Error reading file {}: {}", filepath, e);
            std::process::exit(1);
        }
    }
}

/// Print the content to stdout
fn print_to_stdout(content: &str) {
    println!("{}", content);
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let (filepath,) = parse_args();
    let content = read_file(filepath);
    print_to_stdout(&content);
}
