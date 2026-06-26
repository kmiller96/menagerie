"use client";

import { useState, useMemo, useTransition } from "react";
import { editNote, deleteNote } from "@/lib/actions";
import type { Note } from "@/lib/shared";
import { TAG_PATTERN, timeAgo } from "@/lib/shared";
import { useRouter, useSearchParams } from "next/navigation";

export function NoteList({
  notes,
  allTags,
  hasActiveFilters = false,
}: {
  notes: Note[];
  allTags: { id: number; name: string }[];
  hasActiveFilters?: boolean;
}) {
  if (notes.length === 0) {
    return (
      <p className="text-gray-500">
        {hasActiveFilters
          ? "No notes match your search or filters."
          : "No notes yet. Write one above!"}
      </p>
    );
  }

  return (
    <div className="space-y-3">
      {notes.map((note) => (
        <NoteItem key={note.id} note={note} allTags={allTags} />
      ))}
    </div>
  );
}

function NoteItem({
  note,
  allTags,
}: {
  note: Note;
  allTags: { id: number; name: string }[];
}) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [editing, setEditing] = useState(false);
  const [body, setBody] = useState(note.body);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [isPending, startTransition] = useTransition();

  const tagNameToId = useMemo(
    () => new Map(allTags.map((t) => [t.name.toLowerCase(), t.id])),
    [allTags],
  );

  function handleTagClick(tagName: string) {
    const tagId = tagNameToId.get(tagName.toLowerCase());
    if (tagId === undefined) return;
    const params = new URLSearchParams(searchParams.toString());
    params.set("tags", String(tagId));
    router.push(`?${params.toString()}`);
  }

  function renderBody(text: string) {
    const parts = text.split(TAG_PATTERN);
    return parts.map((part, i) => {
      const match = part.match(/^#([\w-]+)$/i);
      if (match) {
        return (
          <button
            key={i}
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              handleTagClick(match[1]);
            }}
            className="text-blue-600 hover:text-blue-800 font-medium cursor-pointer"
          >
            {match[0]}
          </button>
        );
      }
      return part;
    });
  }

  async function handleSave() {
    startTransition(async () => {
      await editNote(note.id, body);
      setEditing(false);
      router.refresh();
    });
  }

  function handleCancel() {
    setBody(note.body);
    setEditing(false);
  }

  async function handleDelete() {
    startTransition(async () => {
      await deleteNote(note.id);
      router.refresh();
    });
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border p-4 sm:p-5 space-y-3 hover:shadow-md transition-shadow">
      {editing ? (
        <>
          <textarea
            value={body}
            onChange={(e) => setBody(e.target.value)}
            className="w-full border rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-shadow"
            rows={3}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleSave();
              }
            }}
          />
          <div className="flex gap-2">
            <button
              onClick={handleSave}
              disabled={isPending}
              className="bg-green-500 text-white px-4 py-1.5 rounded-lg text-sm font-medium disabled:opacity-50 disabled:cursor-not-allowed transition-colors hover:bg-green-600 active:bg-green-700"
            >
              {isPending ? "Saving..." : "Save"}
            </button>
            <button
              onClick={handleCancel}
              className="bg-gray-100 text-gray-700 px-4 py-1.5 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors"
            >
              Cancel
            </button>
          </div>
        </>
      ) : (
        <>
          <p className="whitespace-pre-wrap leading-relaxed">{renderBody(note.body)}</p>
          <div className="flex items-center justify-between text-sm text-gray-500 pt-1">
            <span suppressHydrationWarning>{timeAgo(note.created_at)}</span>
            <div className="flex gap-3">
              <button
                onClick={() => {
                  setBody(note.body);
                  setEditing(true);
                }}
                className="text-blue-500 hover:text-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium"
                disabled={isPending}
              >
                edit
              </button>
              {confirmDelete ? (
                <>
                  <button
                    onClick={handleDelete}
                    disabled={isPending}
                    className="text-red-600 font-semibold disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                  >
                    {isPending ? "Deleting..." : "Confirm delete?"}
                  </button>
                  <button
                    onClick={() => setConfirmDelete(false)}
                    disabled={isPending}
                    className="text-gray-500 hover:text-gray-700 disabled:opacity-50 transition-colors"
                  >
                    cancel
                  </button>
                </>
              ) : (
                <button
                  onClick={() => setConfirmDelete(true)}
                  disabled={isPending}
                  className="text-red-500 hover:text-red-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium"
                >
                  del
                </button>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}


