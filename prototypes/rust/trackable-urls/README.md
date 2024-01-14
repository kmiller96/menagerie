# Trackable URLs

Exploring how you might come up with a service that tracks when (and if) a user
clicks on a link.

```bash
make serve
```

This prototype ultimately just implements the ID -> document mapping logic. This
isn't really the objective, but next steps from here are pretty trivial and
straight forward. Don't believe I'd learn a lot from it.

To implement:

- Move the mapping into a SQLite database (e.g. `documents` table) that maps the
  ID to a path in the OS for the document. You could also potentially just store
  the documents in the database itself.
- Have a table that logs the access request into the database with relevant
  information (when it was accessed, etc.)

There are, of course, 100 other extensions to this problem. But this is the crux
of it.

I might come back to this prototype and finish it later. But for now, I'm done!
