# Link Shortener MVP

Next.js + Prisma link shortener with redirect analytics.

## Local Development (SQLite)

1. Install deps: `pnpm install`
2. Copy env: `cp .env.example .env`
3. Run migrations: `pnpm db:migrate:sqlite`
4. Start app: `pnpm dev`

## Postgres Cutover (Pre-Launch)

Use a Postgres connection string in `.env`:

```env
DATABASE_URL="postgresql://USER:PASSWORD@HOST:5432/DB?sslmode=require"
```

Then run:

1. `pnpm db:migrate:postgres`
2. `pnpm db:smoke:postgres`

This uses:
- `prisma/schema.postgres.prisma`
- `prisma/migrations-postgres`

## Migration Path: SQLite -> Postgres

Current path is schema-compatible cutover:

1. Keep local development/tests on SQLite.
2. Apply equivalent schema migrations to Postgres with `pnpm db:migrate:postgres`.
3. Verify DB connectivity with `pnpm db:smoke:postgres`.
4. Switch deployment `DATABASE_URL` to Postgres.

No production data backfill is needed for MVP because Postgres cutover happens before launch.

## Vercel Config

In Vercel project settings:

1. Set `DATABASE_URL` to your managed Postgres URL.
2. Set build command to:
   `PRISMA_SCHEMA=prisma/schema.postgres.prisma PRISMA_MIGRATIONS_PATH=prisma/migrations-postgres pnpm db:migrate:postgres && pnpm build`

This ensures schema migrations run against Postgres at deploy time.
