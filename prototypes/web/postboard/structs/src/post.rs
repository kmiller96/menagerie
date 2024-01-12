use std::fmt;

use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

use crate::Submission;

/// Data structure representing a post by a user.
#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub struct Post {
    pub id: Option<i32>,
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
            id: None,
            author: author.unwrap_or("Anonymous".to_string()),
            content,
            created: Utc::now(),
        }
    }

    /// Creates a post from a user submission
    pub fn from_submission(submission: Submission) -> Self {
        Self::new(submission.author, submission.content)
    }

    /// Creates a post from a SQLite row
    pub fn from_sqlite_row(row: &rusqlite::Row<'_>) -> rusqlite::Result<Self> {
        Ok(Self::new(
            row.get(1)?,
            row.get(2)?,
            // id: row.get(1)?,
            // author: row.get(2)?,
            // content: row.get(2)?,
            // created: row.get(4)?,
            // TODO: Fix
        ))
    }
}

impl fmt::Display for Post {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // Implement the formatting logic for the Post struct here
        // For example, you can use `write!` macro to format the fields
        write!(f, "@{}: {}", self.author, self.content)
    }
}
