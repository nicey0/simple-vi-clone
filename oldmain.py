import curses
from messages import Message as M
from state import State


def draw_screen(s: State):
    for i, line in enumerate(s.content):
        r = range(min(s.highlighted), max(s.highlighted)+1)
        if i in r:
            s.scr.addstr(i, 0, line[0:s.scr.getmaxyx()[1]], curses.A_REVERSE)
        else:
            s.scr.addstr(i, 0, line[0:s.scr.getmaxyx()[1]])


def increase_cursor(s: State, values: list):
    s.cursor[0] += values[0]
    if s.cursor[0] < 0:
        s.cursor[0] = 0
    elif s.cursor[0] >= len(s.content):
        s.cursor[0] = len(s.content)-1
    if values[1] == 'START':
        s.cursor[1] = 0
    else:
        s.cursor[1] += values[1]
        maxcur = len(s.content[s.cursor[0]])-1
        if s.cursor[1] < 0:
            s.cursor[1] = 0
        elif s.cursor[1] > maxcur:
            s.cursor[1] = maxcur if maxcur > 0 else 0


def main(scr: curses.window):
    s = State(scr, "hello.txt")
    while True:
        s.scr.clear()
        draw_screen(s)
        _debug(s.scr, s.mode, s.cursor, s.highlighted, s.debug)
        s.scr.move(s.cursor[0], s.cursor[1])
        s.scr.refresh()
        m, data = s.mode.process_key(s.scr.getch())
        if m == M.CURSOR:
            increase_cursor(s, data)
        elif m == M.SWITCH:
            s.mode = data()
        elif m == M.BREAK:
            break
        elif m == M.SAVE:
            with open(s.filename, 'w') as f:
                for line in s.content:
                    f.write(line + '\n')
        elif m == M.INSERTL:
            s.content[s.cursor[0]] = data + s.content[s.cursor[0]]
        elif m == M.APPENDL:
            s.content[s.cursor[0]] += data
        elif m == M.INSERT:
            line: str = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[0:s.cursor[1]] + data + \
                line[s.cursor[1]:]
            increase_cursor(s, [0, 1])
        elif m == M.APPEND:
            line: str = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[0:s.cursor[1]+1] + data + \
                line[s.cursor[1]+1:]
            increase_cursor(s, [0, 1])
        elif m == M.DEBUG:
            if data not in s.debug:
                s.debug.append(data)
        # Newline
        if data == '\n':
            for i, line in enumerate(s.content):
                split = line.split('\n')
                split = [s.replace('\n', '') for s in split]
                if len(split) > 1:
                    s.content = s.content[0:i] + split + s.content[i+1:]
            increase_cursor(s, [1, 'START'])
        # Highlighting
        if s.mode.highlights:
            if not s.last_hl:
                s.highlighted[0] = s.cursor[0]
            s.highlighted[1] = s.cursor[0]
        else:
            if s.last_hl:
                s.highlighted = [-1, -1]
        s.last_hl = s.mode.highlights


def _debug(scr: curses.window, *args):
    sargs = str([str(arg) for arg in args])[1:-1]
    scr.addstr(scr.getmaxyx()[0]-1, 1, sargs)


if __name__ == '__main__':
    curses.wrapper(main)

