import curses
from modes.mode import Mode
from modes.normal import Normal
from messages import Message as M

mode: Mode = None

def draw_screen(scr: curses.window):
    pass

def main(scr: curses.window):
    while True:
        scr.clear()
        draw_screen(scr)
        scr.refresh()
        m = mode.process_key(scr.getch())
        if m == M.BREAK:
            break

if __name__ == '__main__':
    curses.wrapper(main)
