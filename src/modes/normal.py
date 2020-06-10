from messages import Message as M
from modes.insert import Insert
from modes.visual import Visual

class Normal:
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
            return (M.SWITCH, Insert)
        elif key == ord('v'):
            return (M.SWITCH, Visual)
