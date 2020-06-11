from curses import KEY_BACKSPACE as BS
import modes.mode as mode
import modes.normal as normal
import messages as m


class Insert(mode.Mode):
    def __init__(self):
        self.highlights = False
        self.allowdchars = [ord(c) for c in "qwertyuiopasdfghjklzxcvbnm" +
                            "QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()[]{}\\" +
                            "|:;\"'<>,./-_+="]

    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (m.Message.SWITCH, normal.Normal)
        elif key in self.allowdchars:
            return (m.Message.INSERT, chr(key))
        else:
            return (m.Message.CONTINUE, 0)

    def __str__(self):
        return "insert"


class Append(Insert):
    def __init__(self):
        super().__init__()

    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (m.Message.SWITCH, normal.Normal)
        elif key in self.allowdchars:
            return (m.Message.APPEND, chr(key))
        else:
            return (m.Message.CONTINUE, 0)

    def __str__(self):
        return "append"
