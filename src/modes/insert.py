from curses import KEY_BACKSPACE as BS
from curses import KEY_ENTER as CR
import modes.mode as mode
import modes.normal as normal
from state import State


class AddText(mode.Mode):
    def __init__(self):
        self.highlights = False
        self.allowdchars = [ord(c) for c in "qwertyuiopasdfghjklzxcvbnm" +
                            "QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()[]{}\\" +
                            "|:;\"'<>,./-_+= "]

    def process_key(self, s: State, key: int) -> tuple:
        if key == BS:
            s.mode = normal.Normal()
        elif key == CR or key == 10 or key == 13:
            self.line_fn(chr(key), s)
            for i, line in enumerate(s.content):
                split = line.split('\n')
                split = [s.replace('\n', '') for s in split]
                if len(split) > 1:
                    s.content = s.content[0:i] + split + s.content[i+1:]
            s.increase_cursor(1, 'start')
        elif key in self.allowdchars:
            self.line_fn(chr(key), s)

    def line_fn(self, char: str, s: State):
        raise NotImplementedError


class Insert(AddText):
    def __init__(self):
        super().__init__()

    def line_fn(self, char: str, s: State):
        line: str = s.content[s.cursor[0]]
        s.content[s.cursor[0]] = line[0:s.cursor[1]] + char + \
            line[s.cursor[1]:]
        s.increase_cursor(0, 1)

    def __str__(self):
        return "insert"


class Append(AddText):
    def __init__(self):
        super().__init__()

    def line_fn(self, char: str, s: State):
        line: str = s.content[s.cursor[0]]
        s.content[s.cursor[0]] = line[0:s.cursor[1]+1] + char + \
            line[s.cursor[1]+1:]
        s.increase_cursor(0, 1)

    def __str__(self):
        return "append"
