# Tasks

Implementation tasks grouped by phase.

---

## Phase 1 — Setup

- [x] Install production deps: `better-sqlite3`
- [x] Install dev deps: `@types/better-sqlite3`, `tailwindcss`, `postcss`,
      `autoprefixer`
- [x] Configure Tailwind (`postcss.config.js`, add `@import "tailwindcss"` to
      `app/globals.css`) — Tailwind v4 uses CSS-first config via `@theme`
      blocks instead of `tailwind.config.ts`, and `tailwindcss/plugin` PostCSS
      plugin instead of v3's `@tailwind` directives
- [x] Create `lib/db.ts` — initialise better-sqlite3, point at `.data/notes.db`,
      expose a `db` singleton
- [x] Create `lib/schema.ts` — run `CREATE TABLE IF NOT EXISTS` for `notes`,
      `tags`, `note_tags` with indexes; call on app startup

---

## Phase 2 — Tag utilities

- [x] Create `lib/tags.ts`:
  - `parseTags(body: string): string[]` — extract `#[\w-]+`, strip `#`,
    lowercase, deduplicate
  - `syncTags(db, noteId: number, tagNames: string[]): void` — insert any
    new tags into `tags`, reconcile `note_tags` (delete removed, insert new)
  - `getAllTags(db): { id: number; name: string }[]` — list all known tags

---

## Phase 3 — Server Actions

- [x] `lib/actions.ts`:
  - `createNote(body: string): Note` — parse tags, INSERT note, sync tags,
    return note
  - `editNote(id: number, body: string): Note` — parse tags, UPDATE note,
    re-sync tags
  - `deleteNote(id: number): void` — DELETE note (tags cleaned via FK CASCADE)

---

## Phase 4 — Page & Components

- [x] Update `app/page.tsx`:
  - Compose form (textarea + submit button)
  - Search bar (controlled input, drives query param)
  - Tag filter pills (click to toggle, drives query param)
  - Note list (server component that reads from DB with filters)
- [x] Compose form — calls `createNote`, resets on success
- [x] Search bar — filters list as user types (client-side nav or
      `router.push` with search param)
- [x] Tag filter pills — fetch all tags, render as buttons, highlight active,
      toggle inclusion; combine with search
- [x] Note list — iterate notes, render body, `created_at`, edit/delete buttons
- [x] Inline edit — clicking edit replaces body with textarea + save/cancel;
      calls `editNote`
- [x] Delete with confirmation — confirm dialog, calls `deleteNote`

---

## Phase 5 — Polish

- [x] Highlight `#tags` in rendered note bodies (distinct colour, clickable)
- [x] Empty state — message when no notes yet, or no results match filter
- [ ] Loading / pending states for Server Actions
- [ ] Responsive layout, clean Tailwind styling throughout
