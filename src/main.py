import curses
from modes.mode import Mode
from modes.normal import Normal
from messages import Message as M

def draw_screen(scr: curses.window, cursor: list, highlighted: list) -> None:
    # Highlighted lines
    for hl in range(min(highlighted), max(highlighted)):
        scr.addstr(hl, 0, " "*scr.getmaxyx()[1], curses.A_REVERSE)

def debug(scr: curses.window, *args):
    sargs = str(args)[1:-1]
    scr.addstr(scr.getmaxyx()[0]-1, 1, sargs)

def main(scr: curses.window) -> None:
    cursor: list = [0, 0] # y, x
    highlighted: list = [0, 0] # start, current
    last_hl: bool = False # if the program was highlighting lines in the last iteration
    mode: Mode = Normal()
    while True:
        scr.clear()
        draw_screen(scr, cursor, highlighted)
        debug(scr, mode, cursor, highlighted)
        scr.move(cursor[0], cursor[1])
        scr.refresh()
        m, data = mode.process_key(scr.getch())
        if m == M.CURSOR:
            cursor[0] += data[0]
            if cursor[0] < 0:
                cursor[0] = 0
            elif cursor[0] > scr.getmaxyx()[0]-1:
                cursor[0] = scr.getmaxyx()[0]-1
            cursor[1] += data[1]
            if cursor[1] < 0:
                cursor[1] = 0
            elif cursor[1] > scr.getmaxyx()[1]-1:
                cursor[1] = scr.getmaxyx()[1]-1
        elif m == M.SWITCH:
            mode = data()
        elif m == M.BREAK:
            break
        # Highlighting
        if mode.highlights:
            if not last_hl:
                highlighted[0] = cursor[0]
            highlighted[1] = cursor[0]
        else:
            if last_hl:
                highlighted = [0, 0]
        last_hl = mode.highlights

if __name__ == '__main__':
    curses.wrapper(main)
