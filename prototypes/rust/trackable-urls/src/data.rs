//! Contains the file retrieval code

use std::collections::HashMap;
use std::fs;
use std::path;
use std::path::PathBuf;

#[derive(Debug)]
pub struct DocumentMap {
    root: path::PathBuf,
    mapping: HashMap<String, String>,
}

impl DocumentMap {
    /// Creates a new empty map
    pub fn new(root: PathBuf) -> Self {
        Self {
            root,
            mapping: HashMap::new(),
        }
    }

    /// Loads a JSON document into the map
    pub fn load(&mut self, path: String) -> &Self {
        let doc = fs::read_to_string(path).expect("Expected file to exist");
        self.mapping = serde_json::from_str(&doc).expect("Expected JSON to be valid");
        self
    }

    /// Retrieves a path from the map
    pub fn get(&self, id: &str) -> Option<PathBuf> {
        let stem = self.mapping.get(id)?;

        let path = if stem.starts_with("/") {
            self.root.join(stem.trim_start_matches("/"))
        } else {
            self.root.join(stem)
        };

        Some(path)
    }
}
