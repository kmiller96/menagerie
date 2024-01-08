use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

use crate::Submission;

/// Data structure representing a post by a user.
#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub struct Post {
    pub author: String,
    pub content: String,
    #[serde(
        serialize_with = "crate::serde::serialize_datetime",
        deserialize_with = "crate::serde::deserialize_datetime_from_string"
    )]
    pub created: DateTime<Utc>,
}

impl Post {
    /// Creates a new post, optionally with an author
    pub fn new(author: Option<String>, content: String) -> Self {
        Self {
            author: author.unwrap_or("Anonymous".to_string()),
            content,
            created: Utc::now(),
        }
    }

    /// Creates a post from a user submission
    pub fn from_submission(submission: Submission) -> Self {
        Self::new(submission.author, submission.content)
    }
}
