import Database from "better-sqlite3";
import path from "node:path";
import fs from "node:fs";

const dataDir = path.join(process.cwd(), ".data");
fs.mkdirSync(dataDir, { recursive: true });

const dbPath = path.join(dataDir, "notes.db");

const globalForDb = globalThis as typeof globalThis & {
  _db?: Database.Database;
};

const db = globalForDb._db ?? new Database(dbPath);
if (process.env.NODE_ENV !== "production") {
  globalForDb._db = db;
}

db.pragma("journal_mode = WAL");
db.pragma("foreign_keys = ON");

export default db;
