"""Validates the puzzle finder works as expected."""

from puzzles.puzzles import PuzzleFinder


def test_can_find_single_line_comment_puzzle():
    """Validates the puzzle finder can find a single line comment puzzle."""

    puzzles = PuzzleFinder().find(
        """
        # [TODO 1] This is a single line comment puzzle.
        """
    )

    assert len(puzzles) == 1


def test_can_find_single_line_docstring_puzzle():
    """Validates the puzzle finder can find a single line docstring puzzle."""

    puzzles = PuzzleFinder().find(
        '''
        """[TODO 1] This is a single line docstring puzzle."""
        '''
    )

    assert len(puzzles) == 1


def test_can_find_inline_puzzle():
    """Validates the puzzle finder can find an inline puzzle."""

    puzzles = PuzzleFinder().find(
        """
        a = f(b, c)  # [TODO 1] This is a single line comment puzzle.
        """
    )

    assert len(puzzles) == 1


def test_can_find_multiple_puzzles():
    """Validates the puzzle finder can find multiple puzzles."""

    puzzles = PuzzleFinder().find(
        """
        # [TODO 1] This is a single line comment puzzle.
        # [TODO 2] This is a single line comment puzzle.
        """
    )

    assert len(puzzles) == 2
