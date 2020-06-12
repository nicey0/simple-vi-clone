import modes.mode as mode
import modes.insert as insert
import modes.visual as visual
from state import State


class Normal(mode.Mode):
    def __init__(self):
        self.highlights = False

    def process_key(self, s: State, key: int) -> tuple:
        if key == ord('j'):
            s.increase_cursor(1, 0)
        elif key == ord('k'):
            s.increase_cursor(-1, 0)
        elif key == ord('h'):
            s.increase_cursor(0, -1)
        elif key == ord('l'):
            s.increase_cursor(0, 1)
        elif key == ord('i'):
            s.mode = insert.Insert()
        elif key == ord('a'):
            s.mode = insert.Append()
        elif key == ord('I'):
            s.mode = insert.InsertLine()
        elif key == ord('A'):
            s.mode = insert.AppendLine()
        elif key == ord('v'):
            s.mode = visual.Visual()
        elif key == ord('q'):
            s.running = False

    def __str__(self):
        return "normal"
