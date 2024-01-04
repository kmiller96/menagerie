extern crate dotenv;
use std::{env, fs, path};

/// The global configuration object used by the application.
///
/// It should be created using the `Config::new()` function, as it will use
/// helpful defaults if values are missing.
#[derive(Debug)]
pub struct Config {
    pub path: path::PathBuf,
}

impl Config {
    /// Will create a new Config object.
    ///
    /// We will first search for values from the environment and, if that fails,
    /// then we will use default values.
    pub fn new() -> Self {
        dotenv::dotenv().ok();

        Self {
            path: if env::var("UPLOADS_PATH").is_ok() {
                path::PathBuf::from(env::var("UPLOADS_PATH").unwrap())
            } else {
                let mut path = env::current_dir().expect("We should be somewhere in the OS.");

                path.push("uploads");
                fs::create_dir_all(&path).expect("We must have permissions to create directory");

                path
            },
        }
    }
}
