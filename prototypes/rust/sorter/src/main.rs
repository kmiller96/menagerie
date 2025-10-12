// ----------- //
// -- Types -- //
// ----------- //

type Path = String;
type PathVec = Vec<Path>;

// --------- //
// -- CLI -- //
// --------- //

use clap::Parser;

/// Sorts folder of files by timestamp.
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Path to the file to process
    path: String,

    /// Depth of directory traversal
    #[arg(short, long, default_value = "1")]
    depth: u32,
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

/// Loads the CLI arguments.
fn parse_cli() -> Args {
    Args::parse()
}

const TEST_PATH: &str = "path/to/file";

/// Discover files in the given path up to the specified depth
fn find(path: &Path, depth: u32) -> PathVec {
    vec![TEST_PATH.to_string()]
}

/// Sorts the given paths based on metadata.
fn sort(paths: &PathVec) -> PathVec {
    paths.clone()
}

/// Migrates files from the old location to the new location.
fn migrate(old: &Path, new: &Path) {
    return ();
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let args = parse_cli();
    let paths = find(&args.path, args.depth);
    let targets = sort(&paths);

    // TODO: Perform move command on each path
    for i in 0..(targets.clone().len()) {
        let p = &paths[i];
        let t = &targets[i];

        migrate(p, t);
    }
}
