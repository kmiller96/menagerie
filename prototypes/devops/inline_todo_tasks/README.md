# Inline TODO tasks

Allows you to specify TODO tasks inline in your codebase and have this script
extract those into a more structure data format.

## Why?

Gives you a centralised location to manage your upcoming work. In particular, 
technical work that is very tightly coupled to the implementation (e.g. 
refactoring).

## Quickstart

```bash
# Extract all puzzles from the path
puzzles extract example/               > PUZZLES.todo
puzzles extract --format=json example/ > PUZZLES.json

# Assign all puzzles IDs 
puzzles assign example/

# Assign IDs and then extract puzzles
puzzles run example/ > PUZZLES.todo
```