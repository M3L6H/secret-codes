class Enigma:
  rotors = {
    "a": {
      "notches": [false, true, false, true, false, false, false, false, false, false, false, false, false, false, false, true, false, false, true, true, false, true, true, true, false, false],
      "wiring": ["o", "h", "m", "j", "l", "c", "s", "v", "y", "x", "q", "g", "w", "k", "f", "p", "n", "d", "z", "t", "a", "b", "u", "e", "r", "i"]
    },
    "b": {
      "notches": [false, false, true, true, true, false, true, false, false, true, false, false, false, false, false, true, true, false, true, true, true, true, true, true, false, true],
      "wiring": ["k", "g", "p", "o", "y", "s", "j", "t", "q", "c", "z", "f", "m", "n", "l", "w", "i", "x", "e", "h", "u", "b", "d", "v", "a", "r"]
    },
    "c": {
      "notches": [true, false, true, true, true, false, true, true, false, true, true, false, false, false, false, false, false, false, false, true, true, true, false, false, false, true],
      "wiring": ["w", "n", "g", "a", "v", "y", "q", "p", "e", "i", "m", "o", "d", "z", "u", "s", "t", "k", "b", "x", "j", "l", "c", "r", "h", "f"]
    },
    "d": {
      "notches": [true, true, true, false, true, false, false, false, true, false, true, false, false, false, false, true, true, false, false, false, true, false, false, false, false, true],
      "wiring": ["z", "q", "d", "j", "f", "h", "r", "g", "m", "y", "w", "i", "t", "n", "b", "a", "p", "l", "x", "v", "s", "e", "k", "u", "o", "c"]
    },
    "e": {
      "notches": [true, true, true, false, true, true, false, true, true, false, false, true, false, true, false, true, false, false, false, true, true, false, true, true, false, true],
      "wiring": ["w", "h", "r", "j", "q", "o", "s", "c", "l", "y", "z", "d", "b", "t", "f", "g", "v", "k", "e", "a", "p", "n", "m", "u", "i", "x"]
    },
    "f": {
      "notches": [false, true, true, false, false, false, false, false, true, false, true, true, false, false, false, false, false, false, false, false, false, true, true, false, false, true],
      "wiring": ["i", "h", "z", "d", "k", "r", "j", "e", "y", "u", "v", "s", "b", "t", "g", "q", "p", "l", "m", "f", "n", "a", "x", "o", "w", "c"]
    },
    "g": {
      "notches": [true, true, false, false, false, false, false, false, true, false, false, true, false, false, false, false, false, true, false, false, false, true, false, false, true, false],
      "wiring": ["a", "y", "n", "v", "t", "l", "c", "r", "f", "o", "s", "g", "x", "w", "i", "j", "b", "z", "m", "p", "h", "u", "d", "k", "q", "e"]
    },
    "h": {
      "notches": [true, true, false, false, true, false, true, false, true, false, false, true, false, false, false, true, true, false, true, false, true, true, false, false, true, false],
      "wiring": ["k", "j", "x", "v", "q", "h", "y", "d", "n", "b", "t", "o", "w", "r", "a", "g", "l", "f", "c", "p", "m", "s", "u", "i", "e", "z"]
    },
    "i": {
      "notches": [true, false, true, false, false, false, true, false, false, false, false, false, false, true, true, true, true, false, true, false, false, true, true, false, true, true],
      "wiring": ["g", "y", "d", "w", "c", "k", "n", "f", "h", "i", "m", "z", "p", "o", "b", "j", "q", "e", "t", "x", "u", "l", "r", "s", "a", "v"]
    },
    "j": {
      "notches": [true, true, true, false, true, false, false, false, false, false, true, false, false, true, true, true, true, true, false, false, false, true, true, true, true, true],
      "wiring": ["h", "x", "z", "j", "c", "i", "s", "l", "o", "y", "n", "t", "w", "k", "r", "q", "u", "m", "e", "a", "g", "p", "v", "d", "b", "f"]
    }
  }