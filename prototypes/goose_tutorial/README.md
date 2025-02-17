# Goose Database Migration Tool

Explores using Goose, a database migration tool that relies on pure SQL.

## Install

I struggled a bit with the installation instructions (https://pressly.github.io/goose/installation/#linux).

In the end I just installed the binary manually using the releases on Github and
manually putting the binary `/usr/local/bin/goose` and running
`sudo chmod +X /usr/local/bin/goose`.

If you'd like to run the commands yourself without the Makefile, run the
following code:

```bash
export GOOSE_DRIVER=sqlite3
export GOOSE_DBSTRING=./db.sqlite3
export GOOSE_MIGRATION_DIR=./migrations
```

## Quickstart

```bash
goose up # or `make migrations`
```

You can check the database using the sqlite3 connector.

```bash
sqlite3 db.sqlite3
```
