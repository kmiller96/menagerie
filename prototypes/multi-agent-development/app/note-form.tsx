"use client";

import { useRef } from "react";
import { createNoteAction } from "@/lib/actions";

export function NoteForm() {
  const formRef = useRef<HTMLFormElement>(null);

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      formRef.current?.requestSubmit();
    }
  }

  return (
    <form
      ref={formRef}
      action={createNoteAction}
      className="flex flex-col gap-2"
    >
      <textarea
        name="content"
        rows={4}
        className="border rounded p-2 resize-none"
        placeholder="Write a note..."
        onKeyDown={handleKeyDown}
      />
      <button
        type="submit"
        className="bg-blue-500 text-white rounded px-4 py-2 self-end"
      >
        Submit
      </button>
    </form>
  );
}
