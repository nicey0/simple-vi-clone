# simple-vi-clone
Simple Vi clone. Not supposed to be used by anyone.

---

## Modes
- Insert
    - \<BS\>: normal mode
    - \<alphabet and symbols\>: add text to content
    -  \<CR\>: insert new line
- Normal
    - j/k/h/l: down/up/left/right
    - x: delete character on cursor
    - X: delete character behind cursor
    - d: delete line
    - y: yank line
    - p: paste last yanked line (below cursor)
    - P: paste last yanked line (on cursor, shift current line down)
    - i: insert mode (behind cursor)
    - I: insert mode (start of line)
    - a: insert mode (in front of cursor)
    - A: insert mode (end of line)
    - v: line visual mode
    - W: save file
    - q: quit
- Visual
    - \<BS\>: normal mode
    - j/k: down/up
    - d: delete all highlighted lines
    - y: yank all highlighted lines

---

## Files
- /src/main.py
    - Controls the modes. Has all the logic code
- /src/messages.py
    - Enum. Contains different message codes for file to file interactions
- /src/state.py
    - Program state
- /src/modes/
    - Processes character and has some basic attributes.
    - /src/modes/mode.py    => base class
    - /src/modes/insert.py  => insert, line-insert, append and line-append mode
    - /src/modes/normal.py  => normal mode
    - /src/modes/visual.py  => visual mode (line-based)
