//! Collection of serialisation/deserialisation functions

use chrono::{DateTime, Utc};
use serde::{Deserialize, Deserializer, Serializer};

/// Serialiser used to format the created time in the feed
pub fn serialize_datetime<S>(dt: &DateTime<Utc>, serializer: S) -> Result<S::Ok, S::Error>
where
    S: Serializer,
{
    serializer.serialize_str(&dt.to_rfc3339())
}

pub fn deserialize_datetime_from_string<'de, D>(deserializer: D) -> Result<DateTime<Utc>, D::Error>
where
    D: Deserializer<'de>,
{
    let datetime_str = String::deserialize(deserializer)?;
    match DateTime::parse_from_rfc3339(&datetime_str) {
        Ok(dt) => Ok(dt.with_timezone(&Utc)),
        Err(err) => Err(serde::de::Error::custom(err.to_string())),
    }
}
