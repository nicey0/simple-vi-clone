import curses
from messages import Message as M
from state import State


def draw_screen(s: State):
    # Highlighted lines
    # for hl in range(min(s.highlighted), max(s.highlighted)):
    #   s.scr.addstr(hl, 0, " "*s.scr.getmaxyx()[1], curses.A_REVERSE)
    for i, line in enumerate(s.content):
        s.scr.addstr(i, 0, line[0:s.scr.getmaxyx()[1]])


def main(scr: curses.window):
    s = State(scr, "hello.txt")
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
            elif s.cursor[0] >= len(s.content):
                s.cursor[0] = len(s.content)-1
            s.cursor[1] += data[1]
            if s.cursor[1] < 0:
                s.cursor[1] = 0
            elif s.cursor[1] > len(s.content[s.cursor[0]])-1:
                s.cursor[1] = len(s.content[s.cursor[0]])-1
        elif m == M.SWITCH:
            s.mode = data()
        elif m == M.BREAK:
            break
        elif m == M.SAVE:
            with open(s.filename, 'w') as f:
                f.writelines(s.content)
        elif m == M.INSERTL:
            s.content[s.cursor[0]] = data + s.content[s.cursor[0]]
        elif m == M.APPENDL:
            s.content[s.cursor[0]] += data
        elif m == M.INSERT:
            line: str = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[0:s.cursor[1]] + data + \
                line[s.cursor[1]:]
            s.cursor[1] += 1
        elif m == M.APPEND:
            line: str = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[0:s.cursor[1]+1] + data + \
                line[s.cursor[1]+1:]
            s.cursor[1] += 1
        # Highlighting
        if s.mode.highlights:
            if not s.last_hl:
                s.highlighted[0] = s.cursor[0]
            s.highlighted[1] = s.cursor[0]
        else:
            if s.last_hl:
                s.highlighted = [0, 0]
        s.last_hl = s.mode.highlights


def _debug(scr: curses.window, *args):
    sargs = str(args)[1:-1]
    scr.addstr(scr.getmaxyx()[0]-1, 1, sargs)


if __name__ == '__main__':
    curses.wrapper(main)
