import { useState } from "react";

import { NotesService } from "./services";
import { Note } from "./types";

import { Navigator } from "./Navigator";
import { Editor } from "./Editor";

export default function App() {
  const notes = new NotesService();

  const [active, setActive] = useState<Note | undefined>(undefined);

  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh" }}>
      <div style={{ backgroundColor: "crimson", width: "20vw" }}>
        <Navigator
          notes={notes.list()}
          onSelect={(metadata) => {
            const match = notes.list().find((note) => note.id == metadata.id);

            if (!match) {
              throw new Error(`Note with id ${metadata.id} not found`);
            }

            if (active) {
              notes.save(active);
            }

            setActive(notes.get(metadata.id));
          }}
        />
      </div>
      <div
        style={{ display: "flex", flexGrow: 1, backgroundColor: "lightblue" }}
      >
        <Editor note={active} />
      </div>
    </div>
  );
}
