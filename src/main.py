import curses
from modes.mode import Mode
from modes.normal import Normal
from messages import Message as M

def draw_screen(scr: curses.window):
    pass

def main(scr: curses.window):
    cursor: list = [0, 0]
    mode: Mode = Mode
    while True:
        scr.clear()
        draw_screen(scr)
        scr.move(cursor[0], cursor[1])
        scr.refresh()
        # m, data = mode.process_key(scr.getch())
        #---Testing-####################################
        m = (M.BREAK)
        key = scr.getch()
        if key == ord('j'):
            m, data = (M.CURSOR, [cursor[0]+1, cursor[1]])
        elif key == ord('k'):
            m, data = (M.CURSOR, [cursor[0]-1, cursor[1]])
        elif key == ord('h'):
            m, data = (M.CURSOR, [cursor[0], cursor[1]-1])
        elif key == ord('l'):
            m, data = (M.CURSOR, [cursor[0], cursor[1]+1])
        #---Testing-####################################
        if m == M.BREAK:
            break
        elif m == M.CURSOR:
            cursor = data
        scr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
