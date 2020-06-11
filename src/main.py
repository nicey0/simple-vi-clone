import curses
from traceback import print_exc
from modes.mode import Mode
from modes.normal import Normal
from messages import Message as M

class Main:
    scr: curses.window
    filename: str
    cursor: list
    highlighted: list
    last_hl: bool
    mode: Mode

    def __init__(self, **kwargs):
        self.scr = curses.initscr()
        self.filename = kwargs.get('filename')
        self.cursor = [0, 0] # y, x
        self.highlighted = [0, 0] # start, current
        self.last_hl = False # if the program was highlighting lines in the last iteration
        self.mode = Normal()

    def draw_screen(self) -> None:
        # Highlighted lines
        for hl in range(min(self.highlighted), max(self.highlighted)):
            self.scr.addstr(hl, 0, " "*self.scr.getmaxyx()[1], curses.A_REVERSE)

    def _debug(self, *args):
        sargs = str(args)[1:-1]
        self.scr.addstr(self.scr.getmaxyx()[0]-1, 1, sargs)

    def main(self):
        while True:
            self.scr.clear()
            self.draw_screen()
            self._debug(self.mode, self.cursor, self.highlighted)
            self.scr.move(self.cursor[0], self.cursor[1])
            self.scr.refresh()
            m, data = self.mode.process_key(self.scr.getch())
            if m == M.CURSOR:
                self.cursor[0] += data[0]
                if self.cursor[0] < 0:
                    self.cursor[0] = 0
                elif self.cursor[0] > self.scr.getmaxyx()[0]-1:
                    self.cursor[0] = self.scr.getmaxyx()[0]-1
                self.cursor[1] += data[1]
                if self.cursor[1] < 0:
                    self.cursor[1] = 0
                elif self.cursor[1] > self.scr.getmaxyx()[1]-1:
                    self.cursor[1] = self.scr.getmaxyx()[1]-1
            elif m == M.SWITCH:
                self.mode = data()
            elif m == M.BREAK:
                break
            # Highlighting
            if self.mode.highlights:
                if not self.last_hl:
                    self.highlighted[0] = self.cursor[0]
                self.highlighted[1] = self.cursor[0]
            else:
                if self.last_hl:
                    self.highlighted = [0, 0]
            self.last_hl = self.mode.highlights

    def run(self):
        try:
            curses.start_color()
            curses.noecho()
            curses.cbreak()
            self.scr.keypad(True)
            self.main()
        except:
            print_exc()
            curses.endwin()

if __name__ == '__main__':
    main = Main()
    main.run()
