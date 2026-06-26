import { listNotes } from "@/lib/db";
import { NoteForm } from "./note-form";

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q } = await searchParams;
  const notes = listNotes(q);

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Notes</h1>
      <NoteForm />

      <form className="mb-6">
        <input
          name="q"
          defaultValue={q ?? ""}
          className="w-full border rounded p-2"
          placeholder="Search notes..."
          autoComplete="off"
        />
      </form>

      {notes.length === 0 ? (
        <p className="text-gray-500">
          {q ? "No notes match your search." : "No notes yet."}
        </p>
      ) : (
        <ul className="space-y-4 mt-8">
          {notes.map((note) => (
            <li key={note.id} className="border rounded p-4">
              <p className="whitespace-pre-wrap">{note.content}</p>
              <p className="text-sm text-gray-500 mt-2">
                {new Date(note.created_at).toLocaleString()}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
