import { useState } from "react";

import { listNotes, getNote } from "./handlers";

import { Navigator } from "./Navigator";
import { Editor } from "./Editor";

export default function App() {
  const notes = listNotes();
  const [active, setActive] = useState(getNote(notes[0].id));

  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh" }}>
      <div style={{ backgroundColor: "crimson", width: "20vw" }}>
        <Navigator
          notes={notes}
          onSelect={(metadata) => {
            const match = notes.find((note) => note.id == metadata.id);

            if (!match) {
              throw new Error(`Note with id ${metadata.id} not found`);
            }

            const note = getNote(metadata.id);
            setActive(note);
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
