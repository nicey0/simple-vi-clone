import curses
import modes.mode as mode
import modes.normal as normal


class State:
    def __init__(self, filename: str = ""):
        self.scr: curses.window = curses.initscr()
        self.filename: str = filename if filename != "" else None
        self.content: list = ["testline0", "testline1", "testline2"]
        self.cursor: list = [0, 0]  # y, x
        self.highlighted: list = [0, 0]  # start, current
        self.last_hl: bool = False  # if the program was highlighting lines in
        # the last iteration
        self.mode: mode.Mode = normal.Normal()