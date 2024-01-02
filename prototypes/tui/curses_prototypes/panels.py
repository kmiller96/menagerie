"""Demos using panels in curses."""

import sys

import curses
import curses.panel

LIGHT_PANEL = 9617
MID_PANEL = 9618
DARK_PANEL = 9619


@curses.wrapper
def main(stdscr: curses.window):
    curses.curs_set(0)

    # Create the windows
    win1 = curses.newwin(10, 20, 0, 0)
    win2 = curses.newwin(10, 20, 2, 4)
    win3 = curses.newwin(10, 20, 4, 8)

    # Create a panel for each window.
    pan1 = curses.panel.new_panel(win1)
    pan2 = curses.panel.new_panel(win2)
    pan3 = curses.panel.new_panel(win3)

    # Set the panel order.
    curses.panel.update_panels()

    # Draw the panels.
    win1.addstr(0, 0, "Panel 1")
    win2.addstr(0, 0, "Panel 2")
    win3.addstr(0, 0, "Panel 3")

    # Draw the borders.
    pan1.window().border()
    pan2.window().border()
    pan3.window().border()

    # Refresh
    win1.noutrefresh()
    win2.noutrefresh()
    win3.noutrefresh()

    curses.doupdate()

    while True:
        c = stdscr.getch()

        if c == curses.ERR:
            continue

        if c == ord("q"):
            sys.exit(0)

        if c in (ord("1"), ord("2"), ord("3")):
            if c == ord("1"):
                pan1.top()
            elif c == ord("2"):
                pan2.top()
            elif c == ord("3"):
                pan3.top()

            curses.panel.update_panels()
            curses.doupdate()
