from curses import KEY_BACKSPACE as BS
import src.modes.mode as mode
import src.modes.normal as normal
import src.messages as m

class Visual(mode.Mode):
    def __init__(self):
        self.highlights = True
    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (m.Message.SWITCH, normal.Normal)
        elif key == ord('j'):
            return (m.Message.CURSOR, [1, 0])
        elif key == ord('k'):
            return (m.Message.CURSOR, [-1, 0])
        else:
            return (m.Message.CONTINUE, 0)
    def __str__(self):
        return "visual"
