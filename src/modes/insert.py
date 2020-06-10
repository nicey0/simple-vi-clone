from curses import KEY_BACKSPACE as BS
from modes.mode import Mode
from modes import normal
from messages import Message as M

class Insert(Mode):
    def __init__(self):
        self.highlights = False
    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (M.SWITCH, normal.Normal)
        else:
            return (M.CONTINUE, 0)
    def __str__(self):
        return "insert"
