# Ralph Loops — Notes App

A simple, local-first note-taking app. The user submits short plain-text notes,
which appear in a reverse-chronological list. Notes support inline `#hashtag`-style
tags and can be searched and filtered. Everything is stored locally in a SQLite
database.

## Tech Stack

| Layer         | Choice                                      |
| ------------- | ------------------------------------------- |
| Framework     | Next.js 16 (App Router)                     |
| Frontend      | React 19, TypeScript, Tailwind CSS          |
| Backend       | Next.js Server Actions + Route Handlers     |
| Database      | SQLite via better-sqlite3 (local `.data/`)  |
| Tooling       | pnpm, Biome                                 |

## Data Model

- **notes** — `id` (auto-increment PK), `body` (TEXT), `created_at`, `updated_at`
- **tags** — `id` (auto-increment PK), `name` (TEXT, UNIQUE)
- **note_tags** — `note_id`, `tag_id` (composite PK, FK with CASCADE)

On every save or edit, `#tags` are extracted from the body via regex
(`/#[\w-]+/gi`), lowercased, deduplicated, and stored as normalized
associations in the junction table.

## Features

1. **Create** — textarea at the top of the page, submitted via Server Action.
2. **List** — all notes displayed newest-first with body text and timestamp.
3. **Edit** — inline editing; clicking "edit" swaps the body for a textarea.
4. **Delete** — confirmation prompt, then removal via Server Action.
5. **Search** — text filter that matches against note bodies (`LIKE '%query%'`).
6. **Tag filter** — clickable tag pills toggle filtering; combined with search.
   Logic: OR (any selected tag matches).
7. **Tags extracted automatically** on every save; all existing tags shown as
   filter chips.

## UI Layout (single column)

```
┌─────────────────────────┐
│  ✏️ Compose (textarea)   │
│  [Submit]                │
├─────────────────────────┤
│  🔍 Search               │
│  [#work] [#personal] …   │
├─────────────────────────┤
│  • Note body #tag        │
│    2 min ago  [edit][del]│
│  • Another note #ideas   │
│    1 hr ago   [edit][del]│
│  …                       │
└─────────────────────────┘
```

## Non-Goals

- No authentication, sync, or cloud storage.
- No rich text / markdown rendering — plain text only.
- No FTS5 full-text search engine (simple `LIKE` is sufficient for MVP).
- No pagination (flat list; can be added later if needed).
