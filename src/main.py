import curses
from state import State
from modes.mode import Mode
from modes.normal import Normal
from sys import argv


def _debug(scr: curses.window, *args):
    sargs = str([str(arg) for arg in args])[1:-1]
    scr.addstr(scr.getmaxyx()[0]-1, 1, sargs)


def draw_screen(s: State):
    for i, line in enumerate(s.content):
        r = range(min(s.highlighted), max(s.highlighted)+1)
        if i in r:
            s.scr.addstr(i, 0, line[0:s.scr.getmaxyx()[1]], curses.A_REVERSE)
        else:
            s.scr.addstr(i, 0, line[0:s.scr.getmaxyx()[1]])


def main(scr: curses.window, filename: str):
    s = State(scr, filename)
    s.mode: Mode = Normal()
    s.running = True
    while s.running:
        s.scr.clear()
        draw_screen(s)
        _debug(s.scr, s.mode, s.cursor, s.highlighted, s.yankl, s.debug)
        s.scr.move(s.cursor[0], s.cursor[1])
        s.scr.refresh()
        s.mode.process_key(s, s.scr.getch())
        # Highlighting
        if s.mode.highlights:
            if not s.last_hl:
                s.highlighted[0] = s.cursor[0]
            s.highlighted[1] = s.cursor[0]
        else:
            if s.last_hl:
                s.highlighted = [-1, -1]
        s.last_hl = s.mode.highlights


if __name__ == '__main__':
    if len(argv) > 1:
        curses.wrapper(main, argv[1])
