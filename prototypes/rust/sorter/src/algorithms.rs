use std::fs;

use crate::types;
use crate::types::{Path, PathVec};

const TEST_PATH: &str = "path/to/file";

/// Discover files in the given path up to the specified depth
pub fn find(path: &Path, depth: u32) -> Result<PathVec, std::io::Error> {
    match fs::read_dir(path) {
        Ok(entries) => {
            return Ok(vec![TEST_PATH.to_string()]);
        }
        Err(e) => {
            return Err(e);
        }
    }
}

/// Sorts the given paths based on metadata.
pub fn sort(paths: &types::PathVec) -> types::PathVec {
    let mut sorted = paths.clone();
    sorted.sort();
    sorted
}

/// Migrates files from the old location to the new location.
pub fn migrate(old: &Path, new: &Path) {
    return ();
}

// ----------- //
// -- Tests -- //
// ----------- //

#[cfg(test)]
mod tests {
    mod find {
        use super::super::find;
        use std::time::{SystemTime, UNIX_EPOCH};

        // -------------------- //
        // -- Setup/Teardown -- //
        // -------------------- //

        fn generate_id() -> String {
            SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .expect("Time went backwards")
                .as_millis()
                .to_string()
        }

        /// Initialises the test directory
        fn setup(id: &String) -> () {
            // Create directories
            const DIRS: [&str; 6] = ["/a", "/b", "/c/d", "/c/e", "/f/g/h", "/x/y/z"];
            for path in DIRS {
                let path = format!("/tmp/{}/{}", id, path);
                std::fs::create_dir_all(path).expect("Failed to create test directory");
            }

            // Create files
            const FILES: [&str; 5] = [
                "/a/1.txt",
                "/b/2.txt",
                "/c/d/3.txt",
                "/c/e/4.txt",
                "/f/g/h/5.txt",
                // NOTE: Deliberately no files in /x/y/z
            ];
            for file in FILES {
                let file = format!("/tmp/{}/{}", id, file);
                std::fs::write(file, "test").expect("Failed to create test file");
            }
        }

        /// Tears down the test directory
        fn teardown(id: &String) -> () {
            std::fs::remove_dir_all(format!("/tmp/{}", id)).unwrap();
        }

        // ----------- //
        // -- Tests -- //
        // ----------- //

        #[test]
        fn error_on_missing_path() {
            let id = generate_id();
            assert_eq!(id, id);
            setup(&id);

            let path = String::from(format!("/tmp/{}/huh", &id));
            let result = find(&path, 3);

            teardown(&id);

            match result {
                Ok(paths) => {
                    panic!("Expected error, but got paths: {:?}", paths);
                }
                Err(_msg) => {
                    assert!(true);
                }
            }
        }

        #[test]
        fn find_all_files() {
            let id = generate_id();
            setup(&id);

            let path = String::from(format!("/tmp/{}", &id));
            let result = find(&path, 3);

            teardown(&id);

            match result {
                Ok(paths) => {
                    assert_eq!(paths.len(), 5);
                }
                Err(msg) => {
                    teardown(&id);
                    panic!("Error occurred: {}", msg);
                }
            };
        }
    }

    mod sort {

        #[test]
        fn sort_always_true() {
            let result = 2 + 2;
            assert_eq!(result, 4);
        }
    }

    mod migrate {

        #[test]
        fn migrate_always_true() {
            let result = 2 + 2;
            assert_eq!(result, 4);
        }
    }
}
