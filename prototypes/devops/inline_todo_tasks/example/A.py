"""First example of a file."""

# [TODO 2] Here is an example of a single-line puzzle.

# [TODO 5] Here is an example of a multi-line puzzle. The package will collect
# comments that proceed the TODO tag until it reachs another puzzle tag or a
# non-comment line.

# We also support a couple other puzzle tags:
# [FIXME 4] This is a fixme puzzle. Useful when something is very broken.
# [BUG 1] This is a bug puzzle.
# [REFACTOR 3] This is a refactor puzzle. Useful when something is working but
#           needs to be reworked.
# [PUZZLE 6] A generic puzzle tag. Useful for non-broken things that need work.

# Note that the previous example doesn't have any whitespace between puzzles!
# The new identifier will delimit the two puzzles (e.g. the NOTE tag.)

# You can configure the exact puzzles (and the puzzle pattern) you want to match
# on in the config file.


def concat(a: str, b: str):
    return a + b  # [TODO 7] Validate that a and b are strings
