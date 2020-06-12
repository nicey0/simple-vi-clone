from curses import KEY_BACKSPACE as BS
import modes.mode as mode
import modes.normal as normal
from state import State


class Visual(mode.Mode):
    def __init__(self):
        self.highlights = True

    def process_key(self, s: State, key: int) -> tuple:
        if key == BS:
            s.mode = normal.Normal()
        elif key == ord('j'):
            s.increase_cursor(1, 0)
        elif key == ord('k'):
            s.increase_cursor(-1, 0)

    def __str__(self):
        return "visual"
