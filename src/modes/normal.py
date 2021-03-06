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
        elif key == ord('d'):
            s.content = s.content[:s.cursor[0]] + s.content[s.cursor[0]+1:]
            if s.content == []:
                s.content.append("")
            s.increase_cursor(0, 'start')
        elif key == ord('i'):
            s.mode = insert.Insert()
        elif key == ord('I'):
            s.increase_cursor(0, 'start')
            s.mode = insert.Insert()
        elif key == ord('a'):
            s.mode = insert.Append()
        elif key == ord('A'):
            s.increase_cursor(0, 'end')
            s.mode = insert.Append()
        elif key == ord('o'):
            # go to end, add newline and enter append mode
            s.increase_cursor(0, 'end')
            insert.Append().process_key(s, ord('\n'))
            s.mode = insert.Append()
        elif key == ord('O'):
            # go to start, add newline, go up and enter append mode
            s.increase_cursor(0, 'start')
            insert.Insert().process_key(s, ord('\n'))
            s.increase_cursor(-1, 0)
            s.mode = insert.Append()
        elif key == ord('v'):
            s.mode = visual.Visual()
        elif key == ord('w'):
            # Save
            with open(s.filename, 'w') as f:
                for line in s.content:
                    f.write(line + '\n')
        elif key == ord('x'):
            line = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[:s.cursor[1]] + line[s.cursor[1]+1:]
            s.increase_cursor(0, 0)
        elif key == ord('X'):
            line = s.content[s.cursor[0]]
            s.content[s.cursor[0]] = line[:s.cursor[1]-1] + line[s.cursor[1]:]
            s.increase_cursor(0, 0)
        elif key == ord('y'):
            s.yank = s.content[s.cursor[0]]
        elif key == ord('p'):
            s.content.insert(s.cursor[0]+1, s.yank)
            s.increase_cursor(1, 'start')
        elif key == ord('P'):
            if s.cursor[0] == 0:
                s.content = [s.yank] + s.content
            else:
                s.content.insert(s.cursor[0], s.yank)
            s.increase_cursor(-1, 'start')
        elif key == ord('q'):
            s.running = False

    def __str__(self):
        return "normal"
