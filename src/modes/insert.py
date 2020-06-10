from curses import KEY_BACKSPACE as BS
from modes.mode import Mode
from modes.normal import Normal
from messages import Message as M

class Insert(Mode):
    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (M.SWITCH, Normal)
