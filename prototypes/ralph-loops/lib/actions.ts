"use server";

import db from "./db";
import { parseTags, syncTags } from "./tags";

export interface Note {
  id: number;
  body: string;
  created_at: string;
  updated_at: string;
}

export function createNote(body: string): Note {
  const trimmed = body.trim();
  if (!trimmed) throw new Error("Note body cannot be empty");

  const result = db
    .prepare("INSERT INTO notes (body) VALUES (?)")
    .run(trimmed);

  const note = db
    .prepare("SELECT id, body, created_at, updated_at FROM notes WHERE id = ?")
    .get(result.lastInsertRowid) as Note;

  const tags = parseTags(trimmed);
  if (tags.length > 0) {
    syncTags(db, note.id, tags);
  }

  return note;
}

export function editNote(id: number, body: string): Note {
  const trimmed = body.trim();
  if (!trimmed) throw new Error("Note body cannot be empty");

  db.prepare(
    "UPDATE notes SET body = ?, updated_at = datetime('now') WHERE id = ?",
  ).run(trimmed, id);

  const note = db
    .prepare("SELECT id, body, created_at, updated_at FROM notes WHERE id = ?")
    .get(id) as Note | undefined;

  if (!note) throw new Error("Note not found");

  const tags = parseTags(trimmed);
  syncTags(db, note.id, tags);

  return note;
}

export function deleteNote(id: number): void {
  const result = db.prepare("DELETE FROM notes WHERE id = ?").run(id);
  if (result.changes === 0) throw new Error("Note not found");
}
