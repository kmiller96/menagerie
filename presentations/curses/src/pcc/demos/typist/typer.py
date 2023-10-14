"""Object representing the typing interface in the Typist game."""

import sys
import curses
import random

from .structs import Buffer, History


class Typer:
    """User interface to play the typing game."""

    window: "curses.window"
    history_window: "curses.window"
    input_window: "curses.window"

    BACKSPACE_KEYS = ("KEY_BACKSPACE", "^?", "\b", "\x7f")
    ENTER_KEYS = ("KEY_ENTER", "\n", "\r")
    ESCAPE_KEYS = ("KEY_ESCAPE", "\x1b")

    def __init__(self, wordlist: list[str]) -> None:
        self.wordlist = wordlist
        self.pick_word()

        self.buffer: Buffer
        self.history: History

    def pick_word(self):
        """Picks a new word from the wordlist."""
        self.current_word = random.choice(self.wordlist)

    def init(self, window: "curses.window"):
        """Configures the curses runtime."""

        ## Configure curses
        self.window = window
        curses.curs_set(0)
        self.window.nodelay(True)

        ## Define the subwindows of the main window
        window_height, window_width = self.window.getmaxyx()

        history_height = window_height - 3
        history_width = window_width
        history_y, history_x = 0, 0

        self.history_window = self.window.subwin(
            history_height, history_width, history_y, history_x
        )

        input_height = 3
        input_width = window_width
        input_y, input_x = window_height - input_height, 0

        self.input_window = self.window.subwin(
            input_height, input_width, input_y, input_x
        )

        ## Configure data structures
        self.buffer = Buffer()
        self.history = History(max_size=history_height - 2)

        return self

    def handle_input(self):
        """Handle user input."""
        try:
            return self.window.getkey()
        except curses.error:
            return None

    def update(self):
        """Updates the internal state of the typer object."""
        key = self.handle_input()

        if key is None:
            return

        elif key in self.BACKSPACE_KEYS:
            self.buffer.pop()

        elif key in self.ENTER_KEYS:
            self.history.append(str(self.buffer))
            self.buffer.clear()
            self.pick_word()

        elif key in self.ESCAPE_KEYS:
            sys.exit(0)

        else:
            self.buffer.append(key)

    def draw(self):
        """Renders the typer object to the screen."""

        # TODO: Below styling
        # If correct, print user input in green
        # If incorrect, print user input in red
        # If the word is completed, newline and print the next word in grey

        for win in (self.history_window, self.input_window):
            win.erase()
            win.border()

        for i, word in enumerate(self.history):
            height, _ = self.history_window.getmaxyx()
            self.history_window.addstr(height - i - 2, 1, word)

        self.input_window.addstr(1, 1, str(self.buffer))

        for win in (self.history_window, self.input_window):
            win.noutrefresh()
