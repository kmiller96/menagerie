import { NoteMetadata } from "./types";

/** Shows all of the available notes in the editor. */
export function Navigator({
  notes,
  onSelect,
}: {
  notes: NoteMetadata[];
  onSelect: (note: NoteMetadata) => void;
}) {
  return (
    <div
      style={{
        margin: "0px 10px",
      }}
    >
      <h1>Notes</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "10px",
        }}
      >
        {notes.map((note) => (
          <a
            key={note.id}
            href={`#${note.id}`}
            onClick={() => onSelect(note)}
            style={{ margin: 0, padding: 0 }}
          >
            {note.id}
          </a>
        ))}
      </div>
    </div>
  );
}
