use serde::{Deserialize, Serialize};

/// Data structure representing a submission
#[derive(Debug, Serialize, Deserialize)]
pub struct Submission {
    pub author: Option<String>,
    pub content: String,
}
