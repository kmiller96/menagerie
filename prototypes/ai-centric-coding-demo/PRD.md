# Link Shortener MVP PRD

## Summary
Build a public, no-auth link shortener MVP in the existing Next.js app, with:
- Auto-generated short codes only
- Redirect + click counting (timestamp events only)
- Single-page UI for create + recent links
- Core-path automated tests
- Deployment target: Vercel

Constraint resolution:
- SQLite first for development
- Pre-release migration gate to Postgres for production persistence on Vercel

## Architecture & Scope
- Framework: Next.js App Router
- Runtime: Node.js server runtime for API/redirect handlers
- Data access: Prisma ORM
- Storage:
  - Dev: SQLite (`prisma/dev.db`)
  - Pre-release/prod: Postgres (Neon/Supabase/RDS-compatible)
- Auth: none
- Abuse controls: none (deferred)
- Expiration: none
- Admin UI/tools: none in V1

## Public Interfaces

### Routes
1. `POST /api/links`
- Purpose: create short link
- Request JSON:
  - `url: string` (required, absolute URL with `http`/`https`)
- Response `201` JSON:
  - `id: string`
  - `slug: string`
  - `shortUrl: string`
  - `targetUrl: string`
  - `createdAt: string (ISO)`
- Errors:
  - `400` invalid URL
  - `500` internal failure

2. `GET /api/links?limit=20`
- Purpose: list recent links for UI
- Response `200` JSON array:
  - `id, slug, targetUrl, createdAt, clickCount`

3. `GET /s/{slug}`
- Purpose: resolve + redirect
- Behavior:
  - If found: atomically increment `clickCount`, insert click event, return `307` redirect to `targetUrl`
  - If not found: `404` page

### Data Model
1. `Link`
- `id` (cuid, PK)
- `slug` (unique, indexed)
- `targetUrl` (text)
- `clickCount` (int, default 0)
- `createdAt` (datetime default now)

2. `ClickEvent`
- `id` (cuid, PK)
- `linkId` (FK -> Link.id, indexed)
- `clickedAt` (datetime default now)

### Slug Rules
- Auto-generated only
- Alphabet: `[A-Za-z0-9]`
- Length: `7`
- Collision handling: retry generate up to 5 times, then fail with `500`

## Implementation Phases

### Phase 0: Foundation
- Add Prisma + schema + initial migration (SQLite)
- Add env handling (`DATABASE_URL`)
- Add shared validation utilities (URL validator)
- Add typed API response helpers

Deliverable:
- Local DB works, migrations run, app still builds/lints

### Phase 1: Core Backend
- Implement `POST /api/links`
- Implement `GET /api/links`
- Implement `GET /s/[slug]` redirect handler with atomic count increment + event insert
- Add reserved route guard (`api`, `_next`, `favicon.ico`, etc. are not slugs)

Deliverable:
- API and redirect behavior fully functional locally

### Phase 2: Single-Page UI
- Replace `app/page.tsx` with:
  - URL input form + submit
  - Created short link output with copy button
  - “Recent links” list with click counts and timestamps
- Basic loading/error/success states
- Minimal clean styling using existing Tailwind setup

Deliverable:
- End-to-end UX: create -> open short link -> count updates reflected after refresh

### Phase 3: Tests (Core Path Gate)
- Unit tests:
  - URL validation
  - Slug generation format/collision branch
- Integration tests:
  - Create link success/fail
  - Redirect success increments count and logs event
  - Unknown slug returns 404
- Add CI command set:
  - `pnpm lint`
  - `pnpm test`
  - `pnpm build`

Deliverable:
- Green automated checks for core user journeys

### Phase 4: Production Readiness Gate (Required Before Launch)
- Add Postgres Prisma datasource configuration
- Create migration path from SQLite schema to Postgres
- Smoke test on Postgres locally
- Deploy to Vercel with managed Postgres connection string
- Verify persisted redirects/counts after redeploy

Deliverable:
- Durable production persistence compatible with Vercel

## Acceptance Criteria
1. User can submit a valid URL and receive a working `/s/{slug}` link.
2. Visiting `/s/{slug}` redirects correctly and increments total clicks.
3. Click events store timestamp per redirect.
4. Home page shows recent links and current click counts.
5. Invalid URLs are rejected with clear error feedback.
6. Core-path test suite passes in CI.
7. Production deployment uses persistent Postgres storage.

## Testing Scenarios
1. Valid URL (`https://example.com`) creates link.
2. Invalid URL (`foo`, `javascript:...`) rejected.
3. Unknown slug returns 404.
4. Multiple redirects on same slug produce correct `clickCount`.
5. Concurrent redirects do not lose increments.
6. API list endpoint returns newest-first ordering.
7. Production env without `DATABASE_URL` fails fast with clear startup error.

## Assumptions & Defaults
- No authentication or ownership model in MVP.
- No custom aliases, no link expiry, no moderation/admin controls.
- No abuse mitigation in V1 (explicitly deferred).
- Redirect path is `/s/{slug}` (not root-level slug) to avoid route collisions in MVP.
- SQLite is a development accelerator only; Postgres cutover is mandatory pre-launch.

## Delegation Packaging (for AI implementers)
Break work into these implementation tickets:
1. Data layer + Prisma setup
2. Create/list API routes
3. Redirect route + analytics writes
4. Home UI flow
5. Tests + CI scripts
6. Postgres migration + Vercel deploy config

Each ticket must include:
- Files to modify
- Exact acceptance checks
- Commands to verify locally
