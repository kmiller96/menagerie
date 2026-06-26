import Database from "better-sqlite3";
import path from "node:path";
import fs from "node:fs";

let db: Database.Database | undefined;

const DATABASE_DIR = ".data";
const DATABASE_FILE_NAME = "notes.db";

export function getDatabase(): Database.Database {
  if (db) return db; // If the database instance already exists, return it

  // Prepare paths
  const here = process.cwd();
  const dbDir = path.join(here, DATABASE_DIR);
  const dbFilePath = path.join(dbDir, DATABASE_FILE_NAME);

  // Ensure the database directory exists
  fs.mkdirSync(dbDir, { recursive: true });
  db = new Database(dbFilePath);

  // Enable Write-Ahead Logging (WAL) mode and enforce foreign key constraints
  db.pragma("journal_mode = WAL");
  db.pragma("foreign_keys = ON");

  // Return the database instance
  return db;
}
