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
    <form onSubmit={handleSubmit} ref={ref} className="space-y-2">
      <textarea
        name="body"
        placeholder="Write a note..."
        className="w-full border rounded p-2"
        rows={3}
        required
        disabled={isPending}
      />
      <button
        type="submit"
        disabled={isPending}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isPending ? "Submitting..." : "Submit"}
      </button>
    </form>
  );
}
