class Enigma:
  rotors = {
    "a": {
      "notches": [False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, False],
      "wiring": ["o", "h", "m", "j", "l", "c", "s", "v", "y", "x", "q", "g", "w", "k", "f", "p", "n", "d", "z", "t", "a", "b", "u", "e", "r", "i"]
    },
    "b": {
      "notches": [False, False, True, True, True, False, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, True, True, False, True],
      "wiring": ["k", "g", "p", "o", "y", "s", "j", "t", "q", "c", "z", "f", "m", "n", "l", "w", "i", "x", "e", "h", "u", "b", "d", "v", "a", "r"]
    },
    "c": {
      "notches": [True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, True, False, False, False, True],
      "wiring": ["w", "n", "g", "a", "v", "y", "q", "p", "e", "i", "m", "o", "d", "z", "u", "s", "t", "k", "b", "x", "j", "l", "c", "r", "h", "f"]
    },
    "d": {
      "notches": [True, True, True, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True],
      "wiring": ["z", "q", "d", "j", "f", "h", "r", "g", "m", "y", "w", "i", "t", "n", "b", "a", "p", "l", "x", "v", "s", "e", "k", "u", "o", "c"]
    },
    "e": {
      "notches": [True, True, True, False, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, True, False, True],
      "wiring": ["w", "h", "r", "j", "q", "o", "s", "c", "l", "y", "z", "d", "b", "t", "f", "g", "v", "k", "e", "a", "p", "n", "m", "u", "i", "x"]
    },
    "f": {
      "notches": [False, True, True, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True],
      "wiring": ["i", "h", "z", "d", "k", "r", "j", "e", "y", "u", "v", "s", "b", "t", "g", "q", "p", "l", "m", "f", "n", "a", "x", "o", "w", "c"]
    },
    "g": {
      "notches": [True, True, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, False],
      "wiring": ["a", "y", "n", "v", "t", "l", "c", "r", "f", "o", "s", "g", "x", "w", "i", "j", "b", "z", "m", "p", "h", "u", "d", "k", "q", "e"]
    },
    "h": {
      "notches": [True, True, False, False, True, False, True, False, True, False, False, True, False, False, False, True, True, False, True, False, True, True, False, False, True, False],
      "wiring": ["k", "j", "x", "v", "q", "h", "y", "d", "n", "b", "t", "o", "w", "r", "a", "g", "l", "f", "c", "p", "m", "s", "u", "i", "e", "z"]
    },
    "i": {
      "notches": [True, False, True, False, False, False, True, False, False, False, False, False, False, True, True, True, True, False, True, False, False, True, True, False, True, True],
      "wiring": ["g", "y", "d", "w", "c", "k", "n", "f", "h", "i", "m", "z", "p", "o", "b", "j", "q", "e", "t", "x", "u", "l", "r", "s", "a", "v"]
    },
    "j": {
      "notches": [True, True, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True],
      "wiring": ["h", "x", "z", "j", "c", "i", "s", "l", "o", "y", "n", "t", "w", "k", "r", "q", "u", "m", "e", "a", "g", "p", "v", "d", "b", "f"]
    }
  }