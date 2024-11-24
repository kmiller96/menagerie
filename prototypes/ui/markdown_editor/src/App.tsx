import { useState } from "react";

import { NotesService } from "./services";
import { Note } from "./types";

import { Navigator } from "./Navigator";
import { Editor } from "./Editor";

export default function App() {
  const notes = new NotesService();

  const [active, setActive] = useState<Note | undefined>(undefined);
  const [content, setContent] = useState<string | undefined>(undefined);

  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh" }}>
      <div style={{ backgroundColor: "crimson", width: "20vw" }}>
        <Navigator
          notes={notes.list()}
          onSelect={(metadata) => {
            // -- Find the note -- //
            const match = notes.list().find((note) => note.id == metadata.id);
            if (!match) {
              throw new Error(`Note with id ${metadata.id} not found`);
            }

            // -- Load the current note content -- //
            if (active) {
              notes.save({ id: active.id, content: content || "" });
            }

            // -- Change the note -- //
            const newNote = notes.get(metadata.id);

            setActive(newNote);
            setContent(newNote.content);
          }}
        />
      </div>
      <div
        style={{ display: "flex", flexGrow: 1, backgroundColor: "lightblue" }}
      >
        <Editor
          content={content || ""}
          setContent={(newContent: string) => setContent(newContent)}
        />
      </div>
    </div>
  );
}
