from calculator import Calculator
import curses
from curses import wrapper
import startscreen

calc = Calculator()

def main(stdscr):
    running = True
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.keypad(True)
    while running:
        stdscr.clear()
        rows, cols = stdscr.getmaxyx()
        stdscr.addstr(0,0,"Prismatic Calculator - Version 1.0.0" + " "*(cols - 1 - 36), curses.A_REVERSE)
        curses.echo()
        current_index = -1
        for index, item in enumerate(calc.history[::-1]):
            current_index += 1
            if item[1] == None:
                stdscr.addstr(rows-(4+index), 0, f"[{item[2]+1}]: {item[0]}", curses.color_pair(2))
            else:
                if item[3] == True:
                    stdscr.addstr(rows-(4+index), 0, f"{item[1]}", curses.color_pair(1))
                    current_index -= 1
                else:
                    stdscr.addstr(rows-(4+index), 0, f"[{item[2]+1}]: {item[0]} = {item[1]}", curses.color_pair(2))
        stdscr.addstr(rows-3, 0, "-"*(cols-1))
        stdscr.addstr(rows-2, 0, ">>> ")
        expression = stdscr.getstr(rows-2, 4, cols-1).decode("utf-8")

        if expression == "quit":
            break
        else:
            calc.evaluate_expression(expression)
        stdscr.refresh()

wrapper(startscreen.startscren)
wrapper(main)