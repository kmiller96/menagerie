import { Note, NoteMetadata } from "./types";

const NOTES: Note[] = [
  {
    id: "one.md",
    content: undefined,
  },
  {
    id: "two.md",
    content: "Hello, world!",
  },
];

/** Retrieves the list of notes (metadata, not content) */
export function listNotes(): NoteMetadata[] {
  return NOTES.map((note) => {
    return {
      id: note.id,
    };
  });
}

/** Retrieves the content of a note. */
export function getNote(id: string): Note {
  const note = NOTES.find((note) => note.id === id);

  if (!note) {
    throw new Error("Note not found");
  }

  return note;
}
