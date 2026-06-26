"use server";

import { getDatabase } from "./db";
import { parseTags, syncTags } from "./tags";
import type { Note } from "./shared";

const db = getDatabase();

export type { Note };

/** Server action wrapper for creating a note from a form submission. */
export async function createNoteAction(_prevState: unknown, formData: FormData) {
  const body = formData.get("body") as string;
  if (!body?.trim()) return { error: "Note body cannot be empty" };
  await createNote(body.trim());
  return { ok: true };
}

/** Insert a new note and sync its inline tags. */
export async function createNote(body: string): Promise<Note> {
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
    syncTags(note.id, tags);
  }

  return note;
}

/** Update an existing note's body and re-sync its tags. */
export async function editNote(id: number, body: string): Promise<Note> {
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
  syncTags(note.id, tags);

  return note;
}

/** Delete a note by id; throws if the note does not exist. */
export async function deleteNote(id: number): Promise<void> {
  const result = db.prepare("DELETE FROM notes WHERE id = ?").run(id);
  if (result.changes === 0) throw new Error("Note not found");
}
