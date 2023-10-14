"""Simplest possible demo."""

import curses

FPS = 5


def main(stdscr: "curses.window") -> None:
    """Main function."""
    curses.curs_set(0)

    t = -1

    while True:
        t += 1

        stdscr.erase()
        stdscr.addstr(0, 0, f"t = {t}")
        stdscr.refresh()

        curses.napms(1000 // FPS)
