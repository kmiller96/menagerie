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
}

impl fmt::Display for Post {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "@{}: {}", self.author, self.content)
    }
}
