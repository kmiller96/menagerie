"use client";

import { useRef, useTransition } from "react";
import { createNote } from "@/lib/actions";
import { useRouter } from "next/navigation";

export function ComposeForm() {
  const router = useRouter();
  const ref = useRef<HTMLFormElement>(null);
  const [isPending, startTransition] = useTransition();

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const body = formData.get("body") as string;
    if (!body.trim()) return;
    startTransition(async () => {
      await createNote(body);
      ref.current?.reset();
      router.refresh();
    });
  }

  return (
    <form onSubmit={handleSubmit} ref={ref} className="space-y-3 bg-white rounded-xl shadow-sm border p-4 sm:p-5">
      <textarea
        name="body"
        placeholder="Write a note..."
        className="w-full border rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-shadow disabled:bg-gray-100"
        rows={3}
        required
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
