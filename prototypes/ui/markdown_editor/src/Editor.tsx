import { useEffect, useState } from "react";
import { Note } from "./types";

export function Editor({ note }: { note: Note | undefined }) {
  const [value, setValue] = useState<string | undefined>(note?.content);

  useEffect(() => {
    setValue(note?.content);
  }, [note]);

  return (
    <div
      style={{
        padding: "10px 10px",
        flexGrow: 1,
      }}
    >
      <textarea
        style={{
          width: "100%",
          height: "100%",
          border: "none",
          overflow: "auto",
          outline: "none",
          resize: "none",
        }}
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
    </div>
  );
}
