import curses
import modes.mode as mode
import modes.normal as normal


class State:
    def __init__(self, scr: curses.window, filename: str = ""):
        self.scr: curses.window = scr
        self.filename: str = filename if filename != "" else None
        self.content: list = ["testline0", "testline1", "testline2"]
        self.cursor: list = [0, 0]  # y, x
        self.highlighted: list = [-1, -1]  # start, current
        self.last_hl: bool = False  # if the program was highlighting lines in
        # the last iteration
        self.mode: mode.Mode = normal.Normal()
        self.debug: list = []
        self.running: bool = False

    def increase_cursor(self, values: list):
        self.cursor[0] += values[0]
        if self.cursor[0] < 0:
            self.cursor[0] = 0
        elif self.cursor[0] >= len(self.content):
            self.cursor[0] = len(self.content)-1
        if values[1] == 'START':
            self.cursor[1] = 0
        else:
            self.cursor[1] += values[1]
            maxcur = len(self.content[self.cursor[0]])-1
            if self.cursor[1] < 0:
                self.cursor[1] = 0
            elif self.cursor[1] > maxcur:
                self.cursor[1] = maxcur if maxcur > 0 else 0
