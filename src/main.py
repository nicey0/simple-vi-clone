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
    highlighting: bool = True # If true, update highlighted[1] at the end of the
                               # main loop
    highlighted: list = [2, 0] # start, current
    mode: Mode
    while True:
        scr.clear()
        draw_screen(scr, cursor, highlighted)
        # Debug bar
        debug(scr, cursor, highlighted)
        #---Testing-####################################
        scr.move(cursor[0], cursor[1])
        #---Testing-####################################
        scr.refresh()
        # m, data = mode.process_key(scr.getch())
        #---Testing-####################################
        m = M.BREAK
        key = scr.getch()
        # Highlight second line
        if key == ord('j'):
            m, data = (M.CURSOR, [cursor[0]+1, cursor[1]])
        elif key == ord('k'):
            m, data = (M.CURSOR, [cursor[0]-1, cursor[1]])
        elif key == ord('h'):
            m, data = (M.CURSOR, [cursor[0], cursor[1]-1])
        elif key == ord('l'):
            m, data = (M.CURSOR, [cursor[0], cursor[1]+1])
        #---Testing-####################################
        if m == M.CURSOR:
            cursor = data
        elif m == M.BREAK:
            break
        if highlighting:
            highlighted[1] = cursor[0]

if __name__ == '__main__':
    curses.wrapper(main)
