import curses
from state import State


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


def main(scr: curses.window):
    s = State(scr, "hello.txt")
    s.running = True
    while s.running:
        s.scr.clear()
        draw_screen(s)
        _debug(s.scr, s.mode, s.cursor, s.highlighted, s.debug)
        s.scr.move(s.cursor[0], s.cursor[1])
        s.scr.refresh()
        s.mode.process_key(s, s.scr.getch())
        # Save
        if s.filename != "":
            with open(s.filename, 'w') as f:
                for line in s.content:
                    f.write(line + '\n')
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
    curses.wrapper(main)
