import { existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import Database from "better-sqlite3";

const dataDir = join(process.cwd(), ".data");
const dbPath = join(dataDir, "notes.db");

if (!existsSync(dataDir)) {
  mkdirSync(dataDir, { recursive: true });
}

const db = new Database(dbPath);
db.pragma("journal_mode = WAL");

db.exec(`
  CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
  )
`);

export type Note = {
  id: number;
  content: string;
  created_at: string;
  updated_at: string;
};

export function createNote(content: string): Note {
  const stmt = db.prepare("INSERT INTO notes (content) VALUES (?)");
  const result = stmt.run(content);
  return getNote(result.lastInsertRowid as number);
}

export function getNote(id: number): Note {
  const stmt = db.prepare("SELECT * FROM notes WHERE id = ?");
  const note = stmt.get(id) as Note | undefined;
  if (!note) {
    throw new Error(`Note with id ${id} not found`);
  }
  return note;
}

export function listNotes(search?: string): Note[] {
  if (search) {
    const stmt = db.prepare(
      "SELECT * FROM notes WHERE content LIKE ? ORDER BY created_at DESC",
    );
    return stmt.all(`%${search}%`) as Note[];
  }
  const stmt = db.prepare("SELECT * FROM notes ORDER BY created_at DESC");
  return stmt.all() as Note[];
}

export function removeNote(id: number): boolean {
  const stmt = db.prepare("DELETE FROM notes WHERE id = ?");
  const result = stmt.run(id);
  return result.changes > 0;
}

export function editNote(id: number, content: string): Note {
  const stmt = db.prepare(
    "UPDATE notes SET content = ?, updated_at = datetime('now') WHERE id = ?",
  );
  const result = stmt.run(content, id);
  if (result.changes === 0) {
    throw new Error(`Note with id ${id} not found`);
  }
  return getNote(id);
}
