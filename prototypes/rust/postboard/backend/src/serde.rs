//! Defines the serialiser functions for structs

use chrono::{DateTime, Utc};
use rocket::serde::Serializer;

/// Serialiser used to format the created time in the feed
pub fn serialize_datetime<S>(dt: &DateTime<Utc>, serializer: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    serializer.serialize_str(&dt.to_rfc3339())
}
