use clap::Parser;

/// Sorts folder of files by timestamp.
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
pub struct Args {
    /// Path to the file to process
    pub path: String,

    /// Depth of directory traversal
    #[arg(short, long, default_value = "1")]
    pub depth: u32,
}

/// Loads the CLI arguments.
pub fn parse() -> Args {
    Args::parse()
}
