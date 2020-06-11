import src.modes.mode as mode
import src.modes.insert as insert
import src.modes.normal as normal
import src.modes.visual as visual
import src.messages as m

class Normal(mode.Mode):
    def __init__(self):
        self.highlights = False
    def process_key(self, key: int) -> tuple:
        if key == ord('j'):
            return (m.Message.CURSOR, [1, 0])
        elif key == ord('k'):
            return (m.Message.CURSOR, [-1, 0])
        elif key == ord('h'):
            return (m.Message.CURSOR, [0, -1])
        elif key == ord('l'):
            return (m.Message.CURSOR, [0, 1])
        elif key == ord('i'):
            return (m.Message.SWITCH, insert.Insert)
        elif key == ord('v'):
            return (m.Message.SWITCH, visual.Visual)
        elif key == ord('W'):
            return (m.Message.SAVE, 0)
        elif key == ord('q'):
            return (m.Message.BREAK, 0)
        else:
            return (m.Message.CONTINUE, 0)
    def __str__(self):
        return "normal"
