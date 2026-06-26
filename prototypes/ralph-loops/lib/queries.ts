import db from "./db";
import type { Note } from "./shared";

export interface NoteFilters {
  searchQuery?: string;
  selectedTagIds?: number[];
}

/** Fetch notes with optional search text and tag filters. */
export function getNotes(filters: NoteFilters = {}): Note[] {
  const { searchQuery, selectedTagIds } = filters;
  const conditions: string[] = [];
  const params: unknown[] = [];

  if (selectedTagIds && selectedTagIds.length > 0) {
    const placeholders = selectedTagIds.map(() => "?").join(",");
    conditions.push(`n.id IN (SELECT note_id FROM note_tags WHERE tag_id IN (${placeholders}))`);
    params.push(...selectedTagIds);
  }

  if (searchQuery) {
    conditions.push("n.body LIKE ?");
    params.push(`%${searchQuery}%`);
  }

  const select = "SELECT n.id, n.body, n.created_at, n.updated_at FROM notes n";
  const where = conditions.length > 0 ? " WHERE " + conditions.join(" AND ") : "";
  const sql = select + where + " ORDER BY n.created_at DESC";

  return db.prepare(sql).all(...params) as Note[];
}
