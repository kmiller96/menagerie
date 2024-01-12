//! Contains all of the functions to control data access.

use postboard_structs::Post;
use rusqlite::{Connection, Result};

pub struct Database {
    conn: Connection,
}

impl Database {
    /// Creates a new Database object.
    pub fn new() -> Result<Self> {
        let conn = Connection::open_in_memory()?; // TODO: Change to a file

        let mut self_ = Self { conn };
        self_.create_tables()?;
        self_._seed_data()?;

        Ok(self_)
    }

    /// Sets up the tables for the database.
    fn create_tables(&mut self) -> Result<()> {
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                author TEXT NOT NULL,
                content TEXT NOT NULL,
                created DATETIME DEFAULT CURRENT_TIMESTAMP
            )",
            [],
        )?;

        Ok(())
    }

    /// Seeds some fake data into the DB (for testing)
    pub fn _seed_data(&mut self) -> Result<()> {
        let mut statement = self.conn.prepare(
            "INSERT INTO posts (author, content) 
            VALUES (?, ?)",
        )?;

        statement.execute(("Alice", "Hello, world!"))?;
        statement.execute(("Bob", "I am Bob."))?;
        statement.execute(("Charlie", "I am Charlie."))?;

        Ok(())
    }

    /// Returns all of the posts in the database.
    pub fn get_posts(&mut self, limit: u32) -> Result<Vec<Post>> {
        let mut statement = self.conn.prepare(
            "SELECT author, content, created 
            FROM posts 
            ORDER BY created DESC 
            LIMIT ?",
        )?;

        let posts = statement
            .query_map(&[&limit], |row| Post::from_sqlite_row(row))?
            .collect::<Result<Vec<Post>>>()?;

        Ok(posts)
    }
}
