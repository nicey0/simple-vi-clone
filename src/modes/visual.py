from curses import KEY_BACKSPACE as BS
from messages import Message as M
from modes.mode import Mode
from modes import normal
from modes import visual

class Visual(Mode):
    def __init__(self):
        self.highlights = True
    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (M.SWITCH, normal.Normal)
        elif key == ord('j'):
            return (M.CURSOR, [1, 0])
        elif key == ord('k'):
            return (M.CURSOR, [-1, 0])
        else:
            return (M.CONTINUE, 0)
    def __str__(self):
        return "visual"
