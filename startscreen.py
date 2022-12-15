

import curses
from curses import wrapper

line1 = "$$$$$$$\            $$\                                    $$\     $$\           "
line2 = "$$  __$$\           \__|                                   $$ |    \__|          "
line3 = "$$ |  $$ | $$$$$$\  $$\  $$$$$$$\ $$$$$$\$$$$\   $$$$$$\ $$$$$$\   $$\  $$$$$$$\ "
line4 = "$$$$$$$  |$$  __$$\ $$ |$$  _____|$$  _$$  _$$\  \____$$\\_$$  _|  $$ |$$  _____|"
line5 = "$$  ____/ $$ |  \__|$$ |\$$$$$$\  $$ / $$ / $$ | $$$$$$$ | $$ |    $$ |$$ /      "
line6 = "$$ |      $$ |      $$ | \____$$\ $$ | $$ | $$ |$$  __$$ | $$ |$$\ $$ |$$ |      "
line7 = "$$ |      $$ |      $$ |$$$$$$$  |$$ | $$ | $$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$$\ "
line8 = "\__|      \__|      \__|\_______/ \__| \__| \__| \_______|  \____/ \__| \_______|"

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5, (curses.COLS-81) // 2, line1)
    stdscr.addstr(6, (curses.COLS-81) // 2, line2)
    stdscr.addstr(7, (curses.COLS-81) // 2, line3)
    stdscr.addstr(8, (curses.COLS-81) // 2, line4)
    stdscr.addstr(9, (curses.COLS-81) // 2, line5)
    stdscr.addstr(10, (curses.COLS-81) // 2, line6)
    stdscr.addstr(11, (curses.COLS-81) // 2, line7)
    stdscr.addstr(12, (curses.COLS-81) // 2, line8)
    stdscr.addstr(14, (curses.COLS-55) // 2, "A Command line scientific calculator built with python")
    stdscr.addstr(16, (curses.COLS-13) // 2, "Version 1.0.0")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)