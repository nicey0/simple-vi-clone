from messages import Message as M
from modes.mode import Mode
from modes import insert
from modes import visual

class Visual(Mode):
    highlights = True
    def process_key(self, key: int) -> tuple:
        if key == ord('j'):
            return (M.CURSOR, [1, 0])
        elif key == ord('k'):
            return (M.CURSOR, [-1, 0])
        else:
            return (M.CONTINUE,)
