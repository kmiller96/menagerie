"""Simple curses demo where you can change the number through the arrow keys."""

import curses


def main(stdscr: "curses.window") -> None:
    curses.curs_set(0)

    start = 100

    while True:
        stdscr.erase()
        stdscr.addstr(0, 0, f"Count: {start}")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            start += 1
        elif key == curses.KEY_DOWN:
            start -= 1
        elif key == ord("q"):
            break
