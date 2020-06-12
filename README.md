# simple-vi-clone
Simple Vi clone. Not supposed to be used by anyone.

---

## Modes
- Insert
    - (X) \<BS\>: normal mode
    - (X) \<alphabet and symbols\>: add text to content
    - (X)  \<CR\>: insert new line
- Normal
    - (X) j/k/h/l: down/up/left/right
    - (X) x: delete character on cursor
    - (X) X: delete character behind cursor
    - ( ) d: delete line
    - ( ) y: yank line
    - ( ) p: paste last yanked line (below cursor)
    - ( ) P: paste last yanked line (on cursor, shift current line down)
    - (X) i: insert mode (behind cursor)
    - (X) I: insert mode (start of line)
    - (X) a: insert mode (in front of cursor)
    - (X) A: insert mode (end of line)
    - (X) v: line visual mode
    - (X) W: save file
    - (X) q: quit
- Visual
    - (X) \<BS\>: normal mode
    - (X) j/k: down/up
    - ( ) d: delete all highlighted lines
    - ( ) y: yank all highlighted lines

---

## Files
- /src/main.py
    - Manages the modes.
- /src/state.py
    - Program state
- /src/modes/
    - Processes keys
    - /src/modes/mode.py    => base class
    - /src/modes/insert.py  => insert, line-insert, append and line-append mode
    - /src/modes/normal.py  => normal mode
    - /src/modes/visual.py  => visual mode (line-based)
