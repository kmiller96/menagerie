import { createNote, listNotes } from "@/lib/db";

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q } = await searchParams;
  const notes = listNotes(q);

  async function onSubmit(formData: FormData) {
    "use server";
    const content = formData.get("content") as string;
    if (content?.trim()) {
      createNote(content.trim());
    }
  }

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Notes</h1>

      <form action={onSubmit} className="mb-6">
        <textarea
          name="content"
          rows={3}
          className="w-full border rounded p-2 mb-2"
          placeholder="Write a new note..."
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              e.currentTarget.form?.requestSubmit();
            }
          }}
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Add Note
        </button>
      </form>

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
        <ul className="space-y-2">
          {notes.map((note) => (
            <li key={note.id} className="border rounded p-3">
              <p className="whitespace-pre-wrap">{note.content}</p>
              <p className="text-xs text-gray-400 mt-1">
                {new Date(note.created_at).toLocaleString()}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
