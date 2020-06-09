import curses
from modes.mode import Mode
from modes.normal import Normal

def main(scr: curses.window):
    scr.clear()
    scr.addstr("Hello!")
    scr.refresh()
    scr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
