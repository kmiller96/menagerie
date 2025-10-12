use std::fs;
use std::process;

use crate::types;
use crate::types::{Path, PathVec};

const TEST_PATH: &str = "path/to/file";

/// Discover files in the given path up to the specified depth
pub fn find(path: &Path, depth: u32) -> PathVec {
    match fs::read_dir(path) {
        Ok(entries) => {
            println!("{} entries found", entries.count());
            return vec![TEST_PATH.to_string()];
        }
        Err(e) => {
            eprintln!("Error reading directory: {}", e);
            process::exit(1);
        }
    }
}

/// Sorts the given paths based on metadata.
pub fn sort(paths: &types::PathVec) -> types::PathVec {
    paths.clone()
}

/// Migrates files from the old location to the new location.
pub fn migrate(old: &Path, new: &Path) {
    return ();
}
