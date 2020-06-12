import curses
import modes.mode as mode


class State:
    def __init__(self, scr: curses.window, filename: str = ""):
        self.scr: curses.window = scr
        self.filename: str = filename if filename != "" else ".svcNONAME~"
        self.content: list = [""]
        self.cursor: list = [0, 0]  # y, x
        self.highlighted: list = [-1, -1]  # start, current
        self.last_hl: bool = False  # if the program was highlighting lines in
        # the last iteration
        self.mode: mode.Mode = None
        self.debug: list = []
        self.running: bool = False
        self.yank = ""
        self.yankl = []

    def increase_cursor(self, yinc: int, xinc: int):
        try:
            self._cursory(yinc)
            self._cursorx(xinc)
        except IndexError:
            self.cursor[0] = 0
            self.cursor[1] = 0

    def _cursory(self, yinc: int):
        self.cursor[0] += yinc
        if self.cursor[0] < 0:
            self.cursor[0] = 0
        elif self.cursor[0] >= len(self.content):
            self.cursor[0] = len(self.content)-1

    def _cursorx(self, xinc: int):
        maxcur = len(self.content[self.cursor[0]])-1
        if xinc == 'start':
            self.cursor[1] = 0
        elif xinc == 'end':
            self.cursor[1] = maxcur
        else:
            self.cursor[1] += xinc
            if self.cursor[1] < 0:
                self.cursor[1] = 0
            elif self.cursor[1] > maxcur:
                self.cursor[1] = maxcur if maxcur > 0 else 0

