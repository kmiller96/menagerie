import { listNotes } from "@/lib/db";
import { NoteForm } from "./note-form";

export default function Home() {
  const notes = listNotes();

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Notes</h1>
      <NoteForm />
      <ul className="space-y-4 mt-8">
        {notes.map((note) => (
          <li key={note.id} className="border rounded p-4">
            <p className="whitespace-pre-wrap">{note.content}</p>
            <p className="text-sm text-gray-500 mt-2">{note.created_at}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
