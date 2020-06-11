import curses
import src.modes.mode as mode
import src.modes.normal as normal

class State:
    scr: curses.window
    filename: str
    content: list
    cursor: list
    highlighted: list
    last_hl: bool
    mode: mode.Mode

    def __init__(self, filename: str = ""):
        self.scr = curses.initscr()
        self.filename = filename if filename != "" else None
        self.content = ["testline0", "testline1", "testline2"]
        self.cursor = [0, 0] # y, x
        self.highlighted = [0, 0] # start, current
        self.last_hl = False # if the program was highlighting lines in the last iteration
        self.mode = normal.Normal()
