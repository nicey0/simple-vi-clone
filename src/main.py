import curses
from traceback import print_exc
import modes.mode as mode
import modes.normal as normal
from messages import Message as M
from state import State

def draw_screen(s: State):
    # Highlighted lines
    # for hl in range(min(s.highlighted), max(s.highlighted)):
        # s.scr.addstr(hl, 0, " "*s.scr.getmaxyx()[1], curses.A_REVERSE)
    for i, line in enumerate(s.content):
        s.scr.addstr(i+1, 0, line[0:s.scr.getmaxyx()[1]])

def main(s: State):
    while True:
        s.scr.clear()
        draw_screen(s)
        _debug(s.scr, s.mode, s.cursor, s.highlighted)
        s.scr.move(s.cursor[0], s.cursor[1])
        s.scr.refresh()
        m, data = s.mode.process_key(s.scr.getch())
        if m == M.CURSOR:
            s.cursor[0] += data[0]
            if s.cursor[0] < 0:
                s.cursor[0] = 0
            elif s.cursor[0] > s.scr.getmaxyx()[0]-1:
                s.cursor[0] = s.scr.getmaxyx()[0]-1
            s.cursor[1] += data[1]
            if s.cursor[1] < 0:
                s.cursor[1] = 0
            elif s.cursor[1] > s.scr.getmaxyx()[1]-1:
                s.cursor[1] = s.scr.getmaxyx()[1]-1
        elif m == M.SWITCH:
            s.mode = data()
        elif m == M.BREAK:
            end(s)
            break
        elif m == M.SAVE:
            with open(s.filename, 'w') as f:
                for line in s.content:
                    f.write(line)
        # Highlighting
        if s.mode.highlights:
            if not s.last_hl:
                s.highlighted[0] = s.cursor[0]
            s.highlighted[1] = s.cursor[0]
        else:
            if s.last_hl:
                s.highlighted = [0, 0]
        s.last_hl = s.mode.highlights

def run(s: State):
    try:
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        s.scr.keypad(True)
        main(s)
    except:
        end(s)
        print_exc()

def end(s: State):
    s.scr.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

def _debug(scr: curses.window, *args):
    sargs = str(args)[1:-1]
    scr.addstr(scr.getmaxyx()[0]-1, 1, sargs)

if __name__ == '__main__':
    s = State("hello.py")
    run(s)
