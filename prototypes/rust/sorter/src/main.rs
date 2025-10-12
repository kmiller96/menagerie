// ----------- //
// -- Types -- //
// ----------- //

type Path = String;
type PathVec = Vec<Path>;

// ----------------- //
// -- Subroutines -- //
// ----------------- //

/// Loads the CLI arguments.
fn parse_cli() {
    // Read CLI with clap
}

const TEST_PATH: &str = "path/to/file";

/// Discover files in the given path up to the specified depth
fn find(depth: u32) -> PathVec {
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
    let paths = find(3);
    let targets = sort(&paths);

    // TODO: Perform move command on each path
    for i in 0..(targets.clone().len()) {
        let p = &paths[i];
        let t = &targets[i];

        migrate(p, t);
    }
}
