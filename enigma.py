from configparser import ConfigParser
from random import randrange

class Enigma:
  rotors = {
    "a": {
      "notches": [False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, False],
      "wiring": ['>', '^', 'M', 'u', 'n', ' ', 'L', '[', 'i', 'D', '{', 'S', ':', '1', '!', 'G', 'm', 'V', 's', 'g', 'x', '3', 't', 'b', 'X', '~', 'K', '}', '2', 'R', '_', 'y', '.', '`', 'Z', '=', 'C', '*', 'E', 'k', '/', '-', 'H', '5', '%', ']', 'A', 'r', '+', '&', 'p', '#', 'v', 'Q', '"', ')', 'F', 'P', 'w', '4', '$', '\\', 'J', '8', 'l', 'o', '|', 'O', '7', 'W', '9', 'B', 'e', 'j', '?', '(', 'a', 'd', '<', "'", ',', 'z', '@', ';', 'T', '0', 'U', 'c', 'q', 'Y', 'f', 'N', 'h', '6', 'I']
    },
    "b": {
      "notches": [False, False, True, True, True, False, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, True, True, False, True],
      "wiring": ['p', '3', '!', 'O', 'U', '<', 'b', 'q', 'W', 'T', 'l', 'w', 'A', 'i', 'L', 'Z', '|', '~', 'y', '0', 'F', '8', '#', '{', 'o', '?', '4', 'X', '&', 'B', '-', "'", '9', 'C', 'N', 'k', '$', ' ', 'n', '_', 'Y', '(', 'd', '+', '/', 'f', '=', '.', 'e', 'V', '}', '*', 'h', 'K', 'u', 'H', '"', 'S', ':', 'D', '\\', 'I', 'c', 'G', 'J', ',', '`', '2', 'M', ')', 'E', 'x', '1', 'z', 'v', '@', 'r', 'g', 't', ']', '%', '5', 'a', '7', '[', '>', 'm', 'j', 'R', 'P', 's', '6', 'Q', ';', '^']
    },
    "c": {
      "notches": [True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, True, False, False, False, True],
      "wiring": ['"', '#', '{', 'u', ';', 'X', '-', '9', 'n', 't', '?', 'k', '@', 'b', 'A', '%', 'q', '0', '6', 'L', '4', 'C', '&', 'K', 'Y', '=', 'O', 'j', 'o', 'y', ',', '3', 'd', ':', 'F', 'W', ' ', ']', 'l', '(', 'N', 'f', '$', 'w', 'm', 'r', 'p', 'U', 'c', 'G', '.', '[', 'T', "'", 'i', 's', ')', 'Z', '>', 'z', '2', 'h', 'S', 'M', '}', '`', '*', '\\', '^', '|', 'H', '7', 'Q', '5', '8', 'R', 'D', 'a', 'v', 'e', '_', '<', '1', 'P', 'J', '!', '~', 'V', '/', '+', 'I', 'g', 'x', 'B', 'E']
    },
    "d": {
      "notches": [True, True, True, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True],
      "wiring": ['c', '}', '%', 'F', 'x', '*', 'C', '{', 'B', '9', 'e', 'J', 'p', '?', ')', 'Q', '-', '3', 'b', 'j', 'W', 'A', 'L', 'g', 'q', '2', 'o', ':', '_', '@', 'u', '>', 'i', 'Y', 'H', 'h', 'E', ' ', '|', 'z', 'd', 'P', 'm', 'y', 'I', "'", '<', 'l', '=', 'D', '7', 'k', 'U', 't', '\\', '#', 'V', 'G', 'n', 'T', '+', '`', 'S', 'a', 'f', '/', 'O', '"', ']', 'M', '4', '(', 'Z', '!', '.', '~', '1', '6', '5', 'r', 'X', 'w', '0', '8', 'v', ',', '^', 's', '&', '[', '$', ';', 'R', 'N', 'K']
    },
    "e": {
      "notches": [True, True, True, False, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, True, False, True],
      "wiring": ['_', 'N', '~', '&', ']', 'l', '{', 'o', '\\', '}', '"', 'O', '?', "'", 'I', '=', 'F', '.', '3', ':', 'J', '`', 'n', 'j', 'm', 'd', '^', 'U', 'z', 'v', '1', '$', 'i', 'p', ',', '[', '%', 't', 'q', 'w', '0', '<', 'X', '(', 'x', 'a', 'A', 'V', 'M', 'H', '9', '|', 'S', '5', 'E', '2', 'f', ';', 's', 'y', ')', 'B', '!', 'k', 'D', 'Z', '+', 'C', 'R', '#', '>', 'b', 'Q', ' ', '7', 'L', '6', 'u', '-', '/', 'P', 'r', 'T', 'K', 'G', 'e', 'Y', 'c', '8', 'W', '4', 'g', 'h', '*', '@']
    },
    "f": {
      "notches": [False, True, True, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True],
      "wiring": ['W', ' ', '6', ')', '*', 'V', 'R', ':', '~', 'P', 'I', 'e', '.', '!', 'G', '1', 'D', 'B', '@', '2', 'M', 'q', '<', ',', 'n', 'J', '4', '#', 'S', '7', '_', 'r', '9', 'o', 'f', '%', 'j', 's', "'", '\\', 'c', ']', 'k', '=', '0', 'F', '&', '8', 'Z', 'X', 'N', 'w', 'u', '?', 'U', '3', 'v', 'a', '$', '5', 'd', 'g', 'H', '`', 'x', 'l', '[', '/', 'y', ';', 'm', '^', 'L', '"', '>', '(', 'C', 'i', 'E', 'T', 'Y', '}', 'z', '{', 'K', 'A', '-', 'p', 'Q', '|', 'h', 'b', '+', 't', 'O']
    },
    "g": {
      "notches": [True, True, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, False],
      "wiring": ['z', 'm', 'q', 'O', '7', 's', '1', 'p', 'i', '?', '6', 'd', 'Y', 'D', '5', '|', 'j', 'G', 'L', 'N', ' ', '`', 'l', '#', 'f', '[', '/', 'X', '+', 'T', 'B', 'M', '~', 'n', 'W', 'S', '_', '>', 'R', '.', '"', 'Q', 'K', 'y', 'A', '2', 'E', 'J', '0', '{', 'V', '-', '%', '&', '\\', '8', 'k', '@', 'o', '<', '3', 'I', 'F', 'Z', ';', '9', 't', "'", ')', 'v', 'b', 'c', 'H', '^', ',', 'C', '(', 'U', '=', 'e', 'h', '!', '$', '*', 'a', 'r', ']', 'x', 'P', 'u', '4', 'w', 'g', ':', '}']
    },
    "h": {
      "notches": [True, True, False, False, True, False, True, False, True, False, False, True, False, False, False, True, True, False, True, False, True, True, False, False, True, False],
      "wiring": ['!', '*', '}', 'q', '8', 't', 'N', 'e', '|', 'z', ':', 'B', 'y', '%', 'o', 'O', ',', 'R', '#', 'A', '3', '{', '>', 'V', '2', 'H', 'T', 'G', 'I', 'X', '4', '1', '/', '^', 'n', 'S', 'g', 'Y', 'C', 'L', 'U', 'w', 'd', '"', '@', '+', 'v', 'M', '\\', 'j', '[', 'E', 'c', 'p', '5', ')', ';', 'm', '9', 'u', 'P', 'h', 'k', '(', ']', '<', '~', 'J', '7', 'f', '6', "'", '$', '.', 'W', 'Q', '0', 'F', '`', '&', 'i', 'K', 'l', '-', 'a', 'x', 'r', '=', 's', '?', ' ', 'b', 'D', 'Z', '_']
    },
    "i": {
      "notches": [True, False, True, False, False, False, True, False, False, False, False, False, False, True, True, True, True, False, True, False, False, True, True, False, True, True],
      "wiring": ['2', 'W', 'f', '&', 'K', 'P', 'k', 'J', '_', 'M', 'B', '{', '0', 'I', '9', '5', 's', '[', ' ', '/', 'O', ';', 'w', 'N', 'i', ':', 'n', 'e', 'r', 'Z', '>', '$', 'S', 'm', 'F', 'Q', '~', '-', '\\', '6', 'l', '*', 'R', 'o', 'H', '3', '1', '^', 'g', 'q', '`', '4', 'U', '}', 't', 'v', 'E', '?', '#', '!', '.', 'a', '8', '"', 'L', 'X', 'z', '=', '7', 'C', 'V', ']', '(', 'x', 'j', '|', 'Y', '%', 'p', 'u', 'T', 'd', '@', 'b', 'G', "'", ',', '<', 'D', 'c', 'h', ')', 'A', '+', 'y']
    },
    "j": {
      "notches": [True, True, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True],
      "wiring": ['l', 'W', '?', 'c', '\\', '}', '&', 'g', '0', 's', '1', 'n', 'p', 'D', '|', ']', 'x', 'r', 'A', '5', '7', 'J', 'w', 'B', 'u', 'y', '^', 'T', 'Y', '=', ';', '3', ',', 'N', '4', 'F', 'R', 'v', 'E', '6', 'a', 'm', 'O', 'h', "'", '`', '.', '9', '2', 'q', 'o', 'k', '~', ' ', '8', 'Z', 'L', ':', 't', 'z', '[', 'G', '_', 'K', 'C', 'e', '"', 'X', '!', '/', '*', 'V', 'f', '(', '%', '+', 'I', '-', '>', 'P', '$', '@', 'Q', 'b', 'U', 'i', 'S', '{', '<', 'j', ')', '#', 'H', 'd', 'M']
    }
  }

  alphabet = [chr(c) for c in range(32, 127)]
  reflector = ['^', '{', 'Q', ',', 'q', '@', '/', 'y', '-', '_', 'e', 'V', '#', '(', 'x', '&', '7', 'D', 'S', 'O', 'I', 'o', 'c', '0', '`', 'U', 'X', 'J', 'G', 'h', 'T', 'B', '%', 'E', '?', 'K', '1', 'A', '[', '<', 't', '4', ';', 'C', 'W', 'f', '\\', '3', 'm', '"', 'p', '2', '>', '9', '+', 'L', ':', 'w', 'i', 'F', 'N', 'd', ' ', ')', '8', '}', 'n', '6', ']', '*', 'M', 'v', '=', 'Z', '|', 'l', 'k', 'P', 'b', '5', 'R', '$', 's', 'r', 'H', '~', 'g', 'Y', '.', "'", 'z', '!', 'j', 'a', 'u']

  # Converts a character to its position in the alphabet
  @staticmethod
  def char_code(char):
    return ord(char) - 32

  # Gets a random index in the range of Enigma.alphabet that is not among the
  # list of chosen indices
  @staticmethod
  def get_rand_in_alphabet(chosen):
    i = None

    while True:
      i = randrange(0, len(Enigma.alphabet))
      if i not in chosen: break

    return i

  # Generates the "wiring" for a reflector
  @staticmethod
  def create_reflector():
    wiring = [None] * len(Enigma.alphabet)
    chosen = []

    if len(Enigma.alphabet) % 2 == 1:
      chosen.append(randrange(0, len(Enigma.alphabet)))
      wiring[chosen[0]] = Enigma.alphabet[chosen[0]]

    for _ in range(len(Enigma.alphabet) // 2):
      i = Enigma.get_rand_in_alphabet(chosen)
      chosen.append(i)
      j = Enigma.get_rand_in_alphabet(chosen)
      chosen.append(j)
      wiring[i] = Enigma.alphabet[j]
      wiring[j] = Enigma.alphabet[i]

    return wiring

  # Generates the "wiring" for a rotor
  @staticmethod
  def create_rotor():
    wiring = [None] * len(Enigma.alphabet)
    chosen = []

    for i in range(len(Enigma.alphabet)):
      j = Enigma.get_rand_in_alphabet(chosen)
      chosen.append(j)
      wiring[i] = Enigma.alphabet[j]

    return wiring
      

  def __init__(self, config="enigma.ini"):
    self.config = config
    self.load()

  def load(self):
    config = ConfigParser()
    config.read(self.config)

    if len(config.sections()) == 0:
      raise FileNotFoundError(f"Could not find { self.config }")

    self.rotors = [config["rotors"][key] for key in list(config["rotors"])]
    self.rotor_positions = [int(config["rotor positions"][key]) % len(Enigma.alphabet) for key in list(config["rotor positions"])]
    self.plugboard = {}

    for c in [config["plugboard"][k] for k in list(config["plugboard"])]:
      self.plugboard[c[0]] = c[1]
      self.plugboard[c[1]] = c[0]

    self.typex = config["typex"]["enable_typex"].lower() == "true"

  def encode(self, msg):
    return "".join(list(map(self.transform, msg)))

  def transform(self, char):
    if char not in Enigma.alphabet:
      return char

    char = self.plugboard[char] if char in self.plugboard else char

    for i in range(3):
      char = self.pass_through_rotor(char, i)
  
    if self.typex:
      for i in range(2):
        char = self.pass_through_rotor(char, 3 + i)

    char = Enigma.reflector[Enigma.char_code(char)]

    if self.typex:
      for i in range(2):
        char = self.pass_through_rotor(char, 4 - i, True)

    for i in range(3):
      char = self.pass_through_rotor(char, 2 - i, True)

    char = self.plugboard[char] if char in self.plugboard else char

    # Rotate the mechanism
    self.rotate()
    
    return char

  def rotate(self):
    if self.typex:
      if Enigma.rotors[self.rotors[0]]["notches"][self.rotor_positions[0]]:
        if Enigma.rotors[self.rotors[1]]["notches"][self.rotor_positions[1]]:
          self.rotor_positions[2] = (self.rotor_positions[2] + 1) % len(Enigma.alphabet)
        
        self.rotor_positions[1] = (self.rotor_positions[1] + 1) % len(Enigma.alphabet)
      
      self.rotor_positions[0] = (self.rotor_positions[0] + 1) % len(Enigma.alphabet)
    else:
      if self.rotor_positions[0] + 1 == len(Enigma.alphabet):
        if self.rotor_positions[1] + 1 == len(Enigma.alphabet):
          self.rotor_positions[2] = (self.rotor_positions[2] + 1) % len(Enigma.alphabet)
        
        self.rotor_positions[1] = (self.rotor_positions[1] + 1) % len(Enigma.alphabet)
      
      self.rotor_positions[0] = (self.rotor_positions[0] + 1) % len(Enigma.alphabet)

  def pass_through_rotor(self, char, index, rev=False):
    rotor = Enigma.rotors[self.rotors[index]]
    i = (Enigma.char_code(char) + self.rotor_positions[index]) % len(Enigma.alphabet)

    if rev:
      return Enigma.alphabet[rotor["wiring"].index(char) - self.rotor_positions[index]]
    else:
      return rotor["wiring"][i]

enigma = Enigma()
print(enigma.encode("G[.u{b_"))
