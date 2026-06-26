import db from "@/lib/db";
import { getAllTags } from "@/lib/tags";
import { ComposeForm } from "./compose-form";
import { SearchBar } from "./search-bar";
import { TagPills } from "./tag-pills";
import { NoteList } from "./note-list";

interface Props {
  searchParams: Promise<{ q?: string; tags?: string }>;
}

export default async function Home({ searchParams }: Props) {
  const { q, tags } = await searchParams;
  const searchQuery = q ?? "";
  const selectedTagIds = tags
    ? tags.split(",").map(Number).filter((n) => !isNaN(n))
    : [];

  let notes: {
    id: number;
    body: string;
    created_at: string;
    updated_at: string;
  }[];

  if (selectedTagIds.length > 0) {
    const placeholders = selectedTagIds.map(() => "?").join(",");
    const sql = searchQuery
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
    const params = searchQuery
      ? [...selectedTagIds, `%${searchQuery}%`]
      : selectedTagIds;
    notes = db.prepare(sql).all(...params) as typeof notes;
  } else if (searchQuery) {
    notes = db
      .prepare(
        "SELECT id, body, created_at, updated_at FROM notes WHERE body LIKE ? ORDER BY created_at DESC",
      )
      .all(`%${searchQuery}%`) as typeof notes;
  } else {
    notes = db
      .prepare(
        "SELECT id, body, created_at, updated_at FROM notes ORDER BY created_at DESC",
      )
      .all() as typeof notes;
  }

  const allTags = getAllTags(db);

  return (
    <div className="max-w-2xl mx-auto p-4 space-y-4">
      <h1 className="text-2xl font-bold">Notes</h1>
      <ComposeForm />
      <SearchBar initialValue={searchQuery} />
      <TagPills tags={allTags} selectedIds={selectedTagIds} />
      <NoteList notes={notes} allTags={allTags} />
    </div>
  );
}
