import { getDatabase } from "./db";
import { TAG_PATTERN } from "./shared";

const db = getDatabase();

/** Extract unique, lowercased tag names (without `#` prefix) from note body text. */
export function parseTags(body: string): string[] {
  const seen = new Set<string>();
  for (const match of body.matchAll(TAG_PATTERN)) {
    seen.add(match[0].slice(1).toLowerCase());
  }
  return [...seen];
}

/** Replace all tag associations for a note with the given tag names. */
export function syncTags(
  noteId: number,
  tagNames: string[],
): void {
  const tagIds = tagNames.map((name) => {
    db.prepare("INSERT OR IGNORE INTO tags (name) VALUES (?)").run(name);
    const row = db
      .prepare("SELECT id FROM tags WHERE name = ?")
      .get(name) as { id: number } | undefined;
    return row!.id;
  });

  const txn = db.transaction(() => {
    db.prepare("DELETE FROM note_tags WHERE note_id = ?").run(noteId);
    const insertNoteTag = db.prepare(
      "INSERT INTO note_tags (note_id, tag_id) VALUES (?, ?)",
    );
    for (const tagId of tagIds) {
      insertNoteTag.run(noteId, tagId);
    }
  });

  txn();
}

/** Return all tags ordered by name. */
export function getAllTags(): { id: number; name: string }[] {
  return db.prepare("SELECT id, name FROM tags ORDER BY name").all() as {
    id: number;
    name: string;
  }[];
}
