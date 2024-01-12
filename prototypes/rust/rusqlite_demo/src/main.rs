use rusqlite::{Connection, Result};

/// Data structure representing a user in the system
#[allow(dead_code)] // NOTE: We debug print the values, so it isn't dead code.
#[derive(Debug)]
struct User {
    id: i32,
    name: String,
    role: String,
}

fn main() -> Result<()> {
    let users = [["Alice", "Admin"], ["Bob", "User"], ["Charlie", "User"]];

    // Connect to an in-memory DB
    let con = Connection::open_in_memory()?;

    // Create a `users` table
    con.execute(
        "
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        )",
        (),
    )?;

    // Add 3 users to the `users` table
    for user in &users {
        con.execute(
            "
            INSERT INTO users (name, role)
            VALUES (?1, ?2)",
            user,
        )?;
    }

    // Update one of the users
    con.execute(
        "
        UPDATE users
        SET role = 'Admin'
        WHERE name = 'Bob'",
        (),
    )?;

    // Delete one of the users
    con.execute(
        "
        DELETE FROM users
        WHERE name = 'Alice'",
        (),
    )?;

    // Select all of the users and print to the console
    let mut statement = con.prepare("SELECT id, name, role FROM users WHERE role = 'Admin'")?;

    let results = statement.query_map([], |row| {
        Ok(User {
            id: row.get(0)?,
            name: row.get(1)?,
            role: row.get(2)?,
        })
    })?;

    for user in results {
        println!("Found user {:?}", user);
    }

    Ok(())
}
