"use client";

import { useActionState, useRef, useEffect } from "react";
import { createNoteAction } from "@/lib/actions";

export function ComposeForm() {
  const formRef = useRef<HTMLFormElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [state, formAction, isPending] = useActionState(createNoteAction, null);

  useEffect(() => {
    if (state?.ok) {
      formRef.current?.reset();
      textareaRef.current?.focus();
    }
  }, [state]);

  return (
    <form action={formAction} ref={formRef} className="space-y-3 bg-white rounded-xl shadow-sm border p-4 sm:p-5">
      <textarea
        ref={textareaRef}
        name="body"
        placeholder="Write a note..."
        className="w-full border rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-shadow disabled:bg-gray-100"
        rows={3}
        required
        autoFocus
        disabled={isPending}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            (e.currentTarget.form as HTMLFormElement).requestSubmit();
          }
        }}
      />
      <button
        type="submit"
        disabled={isPending}
        className="bg-blue-500 text-white px-5 py-2 rounded-lg hover:bg-blue-600 active:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium"
      >
        {isPending ? "Submitting..." : "Submit"}
      </button>
    </form>
  );
}
