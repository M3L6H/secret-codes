from configparser import ConfigParser
import re

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

  # Converts a character in the range a-z to the range 0-25
  @staticmethod
  def char_code(char):
    return ord(char) - 97

  def __init__(self, config="enigma.ini"):
    self.config = config
    self.load()

  def load(self):
    config = ConfigParser()
    config.read(self.config)

    if len(config.sections()) == 0:
      raise FileNotFoundError(f"Could not find { self.config }")

    self.rotors = [config["rotors"][key] for key in list(config["rotors"])]
    self.rotor_positions = [config["rotor positions"][key] for key in list(config["rotor positions"])]
    self.plugboard = {}

    for c in [config["plugboard"][k] for k in list(config["plugboard"])]:
      self.plugboard[c[0]] = c[1]
      self.plugboard[c[1]] = c[0]

    self.typex = config["typex"]["enable_typex"].lower() == "true"

  def transform(self, char):
    if not re.match(r"^[a-zA-Z]$", char):
      return char

    char = char.lower()

    for i in range(3):
      self.pass_through_rotor(char, i)
  
    if self.typex:
      for i in range(2):
        self.pass_through_rotor(char, 3 + i)
      for i in range(2):
        self.pass_through_rotor(char, 4 - i)

    for i in range(3):
      self.pass_through_rotor(char, 2 - i)

    return self.plugboard[char] if self.plugboard.has_key(char) else char

  def pass_through_rotor(self, char, index):
    rotor = Enigma.rotors[self.rotors[index]]
    char = rotor["wiring"][Enigma.char_code(char)]

enigma = Enigma()