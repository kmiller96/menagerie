use serde::{Deserialize, Serialize};

use super::Post;

/// Data structure representing a submission
#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub struct Submission {
    pub author: Option<String>,
    pub content: String,
}

impl Submission {
    /// Creates a post from a submission
    pub fn to_post(&self) -> Post {
        Post::new(
            self.author.clone().unwrap_or("Anonymous".to_string()),
            self.content.clone(),
        )
    }
}