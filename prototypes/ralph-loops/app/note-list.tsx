"use client";

import { useState, useMemo } from "react";
import { editNote, deleteNote } from "@/lib/actions";
import { useRouter, useSearchParams } from "next/navigation";

interface Note {
  id: number;
  body: string;
  created_at: string;
  updated_at: string;
}

export function NoteList({
  notes,
  allTags,
}: {
  notes: Note[];
  allTags: { id: number; name: string }[];
}) {
  if (notes.length === 0) {
    return <p className="text-gray-500">No notes yet.</p>;
  }

  return (
    <div className="space-y-4">
      {notes.map((note) => (
        <NoteItem key={note.id} note={note} allTags={allTags} />
      ))}
    </div>
  );
}

const TAG_PATTERN = /(#[\w-]+)/gi;

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
    await editNote(note.id, body);
    setEditing(false);
    router.refresh();
  }

  function handleCancel() {
    setBody(note.body);
    setEditing(false);
  }

  async function handleDelete() {
    await deleteNote(note.id);
    router.refresh();
  }

  return (
    <div className="border rounded p-3 space-y-2">
      {editing ? (
        <>
          <textarea
            value={body}
            onChange={(e) => setBody(e.target.value)}
            className="w-full border rounded p-2"
            rows={3}
          />
          <div className="flex gap-2">
            <button
              onClick={handleSave}
              className="bg-green-500 text-white px-3 py-1 rounded text-sm"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="bg-gray-300 px-3 py-1 rounded text-sm"
            >
              Cancel
            </button>
          </div>
        </>
      ) : (
        <>
          <p className="whitespace-pre-wrap">{renderBody(note.body)}</p>
          <div className="flex items-center justify-between text-sm text-gray-500">
            <span>{timeAgo(note.created_at)}</span>
            <div className="flex gap-2">
              <button
                onClick={() => {
                  setBody(note.body);
                  setEditing(true);
                }}
                className="text-blue-500 hover:underline"
              >
                edit
              </button>
              {confirmDelete ? (
                <>
                  <button
                    onClick={handleDelete}
                    className="text-red-600 font-bold"
                  >
                    Confirm delete?
                  </button>
                  <button
                    onClick={() => setConfirmDelete(false)}
                    className="text-gray-500 hover:underline"
                  >
                    cancel
                  </button>
                </>
              ) : (
                <button
                  onClick={() => setConfirmDelete(true)}
                  className="text-red-500 hover:underline"
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

function timeAgo(dateStr: string): string {
  const now = Date.now();
  const date = new Date(dateStr.endsWith("Z") ? dateStr : `${dateStr}Z`).getTime();
  const diff = now - date;
  const minutes = Math.floor(diff / 60000);
  if (minutes < 1) return "just now";
  if (minutes < 60) return `${minutes} min ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours} hr ago`;
  const days = Math.floor(hours / 24);
  return `${days} day${days > 1 ? "s" : ""} ago`;
}
