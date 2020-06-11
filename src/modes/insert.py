from curses import KEY_BACKSPACE as BS
import modes.mode as mode
import modes.normal as normal
import messages as m


class AddText(mode.Mode):
    def __init__(self, addType: int):
        self.highlights = False
        self.allowdchars = [ord(c) for c in "qwertyuiopasdfghjklzxcvbnm" +
                            "QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()[]{}\\" +
                            "|:;\"'<>,./-_+= "]
        self.addType = addType

    def process_key(self, key: int) -> tuple:
        if key == BS:
            return (m.Message.SWITCH, normal.Normal)
        elif key in self.allowdchars:
            return (self.addType, chr(key))
        else:
            return (m.Message.CONTINUE, 0)


class InsertLine(AddText):
    def __init__(self):
        super().__init__(m.Message.INSERTL)

    def __str__(self):
        return "insert_line"


class AppendLine(AddText):
    def __init__(self):
        super().__init__(m.Message.APPENDL)

    def __str__(self):
        return "append_line"


class Insert(AddText):
    def __init__(self):
        super().__init__(m.Message.INSERT)

    def __str__(self):
        return "insert"


class Append(AddText):
    def __init__(self):
        super().__init__(m.Message.APPEND)

    def __str__(self):
        return "append"
