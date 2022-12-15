import curses

line1 = "$$$$$$$\            $$\                                    $$\     $$\           "
line2 = "$$  __$$\           \__|                                   $$ |    \__|          "
line3 = "$$ |  $$ | $$$$$$\  $$\  $$$$$$$\ $$$$$$\$$$$\   $$$$$$\ $$$$$$\   $$\  $$$$$$$\ "
line4 = "$$$$$$$  |$$  __$$\ $$ |$$  _____|$$  _$$  _$$\  \____$$\\_$$  _|  $$ |$$  _____|"
line5 = "$$  ____/ $$ |  \__|$$ |\$$$$$$\  $$ / $$ / $$ | $$$$$$$ | $$ |    $$ |$$ /      "
line6 = "$$ |      $$ |      $$ | \____$$\ $$ | $$ | $$ |$$  __$$ | $$ |$$\ $$ |$$ |      "
line7 = "$$ |      $$ |      $$ |$$$$$$$  |$$ | $$ | $$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$$\ "
line8 = "\__|      \__|      \__|\_______/ \__| \__| \__| \_______|  \____/ \__| \_______|"

def startscren(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    while True:
        rows, cols = stdscr.getmaxyx()
        stdscr.clear()
        stdscr.addstr(5, (cols-81) // 2, line1, curses.color_pair(1))
        stdscr.addstr(6, (cols-81) // 2, line2, curses.color_pair(1))
        stdscr.addstr(7, (cols-81) // 2, line3, curses.color_pair(1))
        stdscr.addstr(8, (cols-81) // 2, line4, curses.color_pair(1))
        stdscr.addstr(9, (cols-81) // 2, line5, curses.color_pair(1))
        stdscr.addstr(10, (cols-81) // 2, line6, curses.color_pair(1))
        stdscr.addstr(11, (cols-81) // 2, line7, curses.color_pair(1))
        stdscr.addstr(12, (cols-81) // 2, line8, curses.color_pair(1))
        stdscr.addstr(14, (cols-55) // 2, "A Command line scientific calculator built with Python")
        stdscr.addstr(16, (cols-13) // 2, "Version 1.0.0", curses.A_UNDERLINE)
        stdscr.addstr(18, (cols-51) // 2, "Made by grqphical07: ")
        stdscr.addstr(18,  (cols-51) // 2 + 21, "https://github.com/grqphical07", curses.color_pair(2))
        stdscr.addstr(20, (cols-65) // 2, "Read the docs here: ")
        stdscr.addstr(20,  (cols-65) // 2 + 20, "https://github.com/grqphical07/Prismatic/wiki", curses.color_pair(2))
        stdscr.addstr(22, (cols-46) // 2, "Press ")
        stdscr.addstr(22, (cols-46) // 2 + 6, "<Enter>", curses.color_pair(2))
        stdscr.addstr(22, (cols-46) // 2 + 13, " To Begin. ")
        stdscr.addstr(22, (cols-46) // 2 + 24, "Press ")
        stdscr.addstr(22, (cols-46) // 2 + 30, "<Escape>", curses.color_pair(2))
        stdscr.addstr(22, (cols-46) // 2 + 38, " To Exit")
        stdscr.refresh()
        key = stdscr.getch()
        if key == 10:
            break
        elif key == 27:
            curses.endwin()
            exit()