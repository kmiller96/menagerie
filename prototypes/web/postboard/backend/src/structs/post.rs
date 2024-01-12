use std::fmt;

use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

/// Data structure representing a post by a user.
#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub struct Post {
    pub id: Option<i32>,
    pub author: String,
    pub content: String,
    #[serde(
        serialize_with = "super::serde::serialize_datetime",
        deserialize_with = "super::serde::deserialize_datetime_from_string"
    )]
    pub created: DateTime<Utc>,
}

impl Post {
    /// Initialises a brand new post
    pub fn new(author: String, content: String) -> Self {
        Self {
            id: None,
            author,
            content,
            created: Utc::now(),
        }
    }

    /// Provides a SQL statement to create the posts table.
    pub fn create_table_statement() -> &'static str {
        "CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            created TIMESTAMP NOT NULL
        )"
    }
}

impl fmt::Display for Post {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "@{}: {}", self.author, self.content)
    }
}
