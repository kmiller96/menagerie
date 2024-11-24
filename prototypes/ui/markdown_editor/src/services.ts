import { Note, NoteMetadata } from "./types";
import { notes } from "./data";

export class NotesService {
  notes: Note[];

  constructor() {
    this.notes = notes;
  }

  public list(): NoteMetadata[] {
    return this.notes.map((note) => {
      return {
        id: note.id,
      };
    });
  }

  public get(id: string): Note {
    const note = this.notes.find((note) => note.id === id);

    if (!note) {
      throw new Error(`Note with id ${id} not found`);
    }

    return note;
  }

  public save(note: Note): void {
    const existingNote = this.notes.find((n) => n.id === note.id);

    if (existingNote) {
      existingNote.content = note.content;
    } else {
      this.notes.push(note);
    }

    return;
  }
}
