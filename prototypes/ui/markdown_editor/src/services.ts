import { Note, NoteMetadata } from "./types";
import { NOTES } from "./data";

export class NotesService {
  notes: Note[];

  constructor() {
    this.notes = NOTES;
  }

  public list(): NoteMetadata[] {
    return this.notes.map((note) => {
      return {
        id: note.id,
      };
    });
  }

  public get(id: string): Note | undefined {
    return this.notes.find((note) => note.id === id);
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
