# simple-vi-clone
Simple Vi clone. Not supposed to be used by anyone.

---

## Modes
- Insert
    - \<BS\>: normal mode
- Normal
    - j/k/h/l: down/up/left/right
    - x: delete character on cursor (cursor shifts to left, like \<BS\>)
    - d: delete line
    - y: yank line
    - p: paste last yanked line
    - i: insert mode (behind cursor)
    - a: insert mode (in front of cursor)
    - v: line visual mode
- Visual
    - j/k: down/up/
    - d: delete all highlighted lines
    - y: yank all highlighted lines

---

## Files
- /src/main.py
    - Controls modes.py. Doesn't have much logic code.
- /src/messages.py
    - Enum. Contains different message codes for file=>file interactions
- /src/modes/
    - Contains most of the logic for each mode. Modes here never interact directly 
    - /src/modes/mode.py    => base class
    - /src/modes/insert.py  => insert mode
    - /src/modes/normal.py  => normal mode
    - /src/modes/visual.py  => visual mode (line-based)
