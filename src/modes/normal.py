from messages import Message as M

class Normal:
    def process_key(self, key: int):
        if key == ord('j'):
            return (M.CURSOR, [1, 0])
        elif key == ord('k'):
            return (M.CURSOR, [-1, 0])
        elif key == ord('h'):
            return (M.CURSOR, [0, -1])
        elif key == ord('l'):
            return (M.CURSOR, [0, 1])
