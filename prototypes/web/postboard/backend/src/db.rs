//! Contains all of the functions to control data access.

use crate::structs::Post;
use rusqlite::{Connection, Result};

use chrono::Utc;

pub struct Database {
    conn: Connection,
}

impl Database {
    /// Creates a new Database object.
    pub fn new() -> Result<Self> {
        let conn = Connection::open_in_memory()?; // TODO: Change to a file

        let mut self_ = Self { conn };
        self_.create_tables()?;
        self_._seed_data()?; // TEMPORARY

        Ok(self_)
    }

    /// Sets up the tables for the database.
    fn create_tables(&mut self) -> Result<()> {
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                author TEXT NOT NULL,
                content TEXT NOT NULL,
                created TIMESTAMP NOT NULL
            )",
            (),
        )?;

        Ok(())
    }

    /// Seeds some fake data into the DB (for testing)
    pub fn _seed_data(&mut self) -> Result<()> {
        let mut statement = self.conn.prepare(
            "INSERT INTO posts (author, content, created) 
            VALUES (?, ?, ?)",
        )?;

        statement.execute(("Alice", "Hello, world!", Utc::now()))?;
        statement.execute(("Bob", "I am Bob.", Utc::now()))?;
        statement.execute(("Charlie", "I am Charlie.", Utc::now()))?;

        Ok(())
    }

    /// Returns all of the posts in the database.
    pub fn get_posts(&mut self, limit: u32) -> Result<Vec<Post>> {
        let mut statement = self.conn.prepare(
            "SELECT id, author, content, created 
            FROM posts 
            ORDER BY created DESC 
            LIMIT ?",
        )?;

        let posts = statement
            .query_map(&[&limit], |row| {
                Ok(Post {
                    id: row.get(0)?,
                    author: row.get(1)?,
                    content: row.get(2)?,
                    created: Utc::now(), // TODO: Load this from the DB
                })
            })?
            .collect::<Result<Vec<Post>>>()?;

        Ok(posts)
    }
}
