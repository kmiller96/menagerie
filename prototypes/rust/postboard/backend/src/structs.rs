//! Defines the data structures for the server

use chrono::{DateTime, Utc};
use rocket::serde::{Serialize, Serializer};

fn serialize_datetime<S>(dt: &DateTime<Utc>, serializer: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    serializer.serialize_str(&dt.to_rfc3339())
}

#[derive(Debug, Serialize)]
pub struct Post {
    author: String,
    content: String,
    // #[serde(serialize_with = "serialize_datetime")]
    // created: DateTime<Utc>,
}

impl Post {
    pub fn new(author: Option<String>, content: String) -> Self {
        Self {
            author: author.unwrap_or("Anonymous".to_string()),
            content,
            // created: Utc::now(),
        }
    }
}
