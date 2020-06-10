from messages import Message as M
from modes.mode import Mode
from modes import insert
from modes import visual

class Normal(Mode):
    highlights = False
    def process_key(self, key: int) -> tuple:
        if key == ord('j'):
            return (M.CURSOR, [1, 0])
        elif key == ord('k'):
            return (M.CURSOR, [-1, 0])
        elif key == ord('h'):
            return (M.CURSOR, [0, -1])
        elif key == ord('l'):
            return (M.CURSOR, [0, 1])
        elif key == ord('i'):
            return (M.SWITCH, insert.Insert)
        elif key == ord('v'):
            return (M.SWITCH, visual.Visual)
        else:
            return (M.CONTINUE,)
