A = 440
Asharp = 466
B = 494
C = 262
Csharp = 277
D = 294
Dsharp = 311
E = 330
F = 349
Fsharp = 370
G = 392
Gsharp = 415

C_higher = 524

note_keys = {
    81: C,  # Q
    65: Csharp,  # A

    87: D,  # W
    83: Dsharp,  # S

    69: E,  # E

    82: F,  # R
    68: Fsharp,  # D

    85: G,  # U
    74: Gsharp,  # J

    73: A,  # I
    75: Asharp,  # K

    79: B,  # O

    80: C_higher,  # P

}

_help_message_1 = """I. Introduction
                                      pynotes by Bennett Nguyen

pynotes is a computer program that turn your computer into a simple music instrument using keylogger!
Every key you pressed will be considered as a command and will instruct this program to do something.
"""

_help_message_2 = """II. Commands for playing notes
Key <KEY>: <MUSICAL-NOTE>

Key Q: C
Key A: C#
Key W: D
Key S: D#
Key E: E
Key R: F
Key D: F#

Key U: G
Key J: G#
Key I: A
Key K: A#
Key O: B
Key P: C (higher pitch)
"""

_help_message_3 = """III. Functional commands
Key <KEY>: <USAGE>
Key <KEY + BINDING>: <USAGE>

Key H: prints out this message
Key Delete: Clear the console
Key C: Decreases the pitch level of all notes (min: 1)
Key N: Increases the pitch level of all notes (max: 16)
Key V: Decreases the duration of playing all notes (min: 0ms)
Key B: Increases the duration of playing all notes (max: 15s)

Key <Ctrl + C>: Exit the program
"""

list_of_message = [_help_message_1, _help_message_2, _help_message_3]
