from curses import KEY_BACKSPACE as BS
import src.modes.mode as mode
import src.modes.normal as normal
import src.messages as m

class Insert(mode.Mode):
    def __init__(self):
        self.highlights = False
    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (m.Message.SWITCH, normal.Normal)
        else:
            return (m.Message.CONTINUE, 0)
    def __str__(self):
        return "insert"
