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

---

# Lessons Learnt

So, did it work? It definitely worked. It works _really_ well. I could see
myself rolling my own solution for my own work.

The big thing that stands out to me is the fact that I have zero idea how any of
this code works. I would have to dig into it to really understand wtf is going
on. Furthermore, there could be 100 bugs in here and I would have no idea. That's
not great when customers are depending on my expertise and assurance...

So to make this work well, I think you'd need to have a tight review process and
cycle. You might not need to do this review every "turn" and could probably
postpone this until a PR or end of day. But you couldn't just YOLO forever.

BUT I do see the potential! The amount of code churned out was amazing for about
5 braincells and 15 minutes of coding.

I would say that you'd also want to have a tighter process around the PRD. I do
think you could collaborate with an AI to write these PRDs, but I think you'd
want to really think about these PRDs and make sure you're happy with the design,
technology choices, etc. I'd argue that _this_ is the IP that you'd develop as
a fCTO and help coach your clients through. Helping with these PRDs would be 90%
of the work and you could just let Codex/Claude wokr from there.

Similar vein, it would be good to get good at sketching using Mermaid and using
Figma so that could be factored into the PRDs. It looks like codex can accept
images: https://developers.openai.com/codex/cli/features/#image-inputs
