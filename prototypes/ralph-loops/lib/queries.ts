import db from "./db";
import type { Note } from "./shared";

export interface NoteFilters {
  searchQuery?: string;
  selectedTagIds?: number[];
}

export function getNotes(filters: NoteFilters = {}): Note[] {
  const { searchQuery, selectedTagIds } = filters;
  const hasTags = selectedTagIds && selectedTagIds.length > 0;
  const hasSearch = !!searchQuery;

  if (hasTags) {
    const placeholders = selectedTagIds!.map(() => "?").join(",");
    const sql = hasSearch
      ? `SELECT DISTINCT n.id, n.body, n.created_at, n.updated_at
         FROM notes n
         JOIN note_tags nt ON n.id = nt.note_id
         WHERE nt.tag_id IN (${placeholders})
           AND n.body LIKE ?
         ORDER BY n.created_at DESC`
      : `SELECT DISTINCT n.id, n.body, n.created_at, n.updated_at
         FROM notes n
         JOIN note_tags nt ON n.id = nt.note_id
         WHERE nt.tag_id IN (${placeholders})
         ORDER BY n.created_at DESC`;
    const params = hasSearch
      ? [...selectedTagIds!, `%${searchQuery}%`]
      : selectedTagIds!;
    return db.prepare(sql).all(...params) as Note[];
  }

  if (hasSearch) {
    return db
      .prepare(
        "SELECT id, body, created_at, updated_at FROM notes WHERE body LIKE ? ORDER BY created_at DESC",
      )
      .all(`%${searchQuery}%`) as Note[];
  }

  return db
    .prepare(
      "SELECT id, body, created_at, updated_at FROM notes ORDER BY created_at DESC",
    )
    .all() as Note[];
}
