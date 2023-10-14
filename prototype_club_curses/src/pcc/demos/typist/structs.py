"""Custom data structures for the typist game."""


class Buffer:
    """Buffer used to store the user input."""

    def __init__(self) -> None:
        self._buffer = []

    def __str__(self) -> str:
        return "".join(self._buffer)

    def append(self, key: str) -> None:
        """Appends a key to the buffer."""
        self._buffer.append(key)

    def pop(self) -> None:
        """Pops a key from the buffer."""
        if len(self._buffer) > 0:
            return self._buffer.pop()
        else:
            return None

    def clear(self) -> None:
        """Clears the buffer."""
        self._buffer.clear()


class History:
    """Buffer of historical values."""

    def __init__(self, max_size: int) -> None:
        self._max_size = max_size
        self._history = []

    def __len__(self):
        return len(self._history)

    def __iter__(self):
        return iter(self._history[::-1])

    def append(self, value: str) -> None:
        """Appends a value to the history."""
        self._history.append(value)

        if len(self._history) > self._max_size:
            self._history.pop(0)

    def previous(self, n: int) -> str:
        """Returns the previous value in the history."""
        if len(self._history) < n:
            return None

        return self._history[-n]
