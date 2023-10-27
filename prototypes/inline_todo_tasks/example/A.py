"""First example of a file."""

# [TODO] Here is an example of a single-line puzzle.

# [TODO] Here is an example of a multi-line puzzle. The package will collect
# comments that proceed the TODO tag until it reachs another puzzle tag or a
# non-comment line.

# We also support a couple other puzzle tags:
# [FIXME] This is a fixme puzzle. Useful when something is very broken.
# [BUG] This is a bug puzzle.
# [REFACTOR] This is a refactor puzzle. Useful when something is working but
#           needs to be reworked.
# [PUZZLE] A generic puzzle tag. Useful for non-broken things that need work.

# Note that the previous example doesn't have any whitespace between puzzles!
# The new identifier will delimit the two puzzles (e.g. the NOTE tag.)

# You can configure the exact puzzles (and the puzzle pattern) you want to match
# on in the config file.


def concat(a: str, b: str):
    return a + b  # [TODO] Validate that a and b are strings
