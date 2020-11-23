from configparser import ConfigParser
from random import randrange

class Enigma:
  rotors = {
    "a": {
      "notches": [False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, True, True, True, False, False],
      "wiring": ['{', 'P', '8', 'z', 'T', 'p', '5', 'i', '=', '6', '9', 'x', '\\', 'Y', '~', 'L', '@', 'N', '<', 'r', 'W', '&', ')', 'Q', '"', '*', 'A', 'y', '2', '(', 'b', 't', '0', ':', 'X', 'l', 'a', 'Z', 'j', 'm', 'k', '|', '^', '`', '/', 'n', '1', 'g', '!', '7', 'h', 'u', '$', 'c', 'd', '4', 'B', '-', 'E', 'q', ',', '_', 'J', ']', 'K', 'D', '>', 'U', 'V', 'v', 'w', 'O', 'R', "'", 'F', 'H', 'C', 'G', 'M', 'o', '%', '[', '3', '}', '?', 'S', 'e', 'f', '+', ';', '#', ' ', 'I', 's', '.']
    },
    "b": {
      "notches": [False, False, True, True, True, False, True, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, True, True, False, True],
      "wiring": ['3', 'N', '5', 'p', 'K', 'M', '(', 'U', '&', '=', '[', 'V', 'Y', 'h', '8', 'C', 'B', '4', 'Z', ' ', '1', '"', 'X', 'G', '.', 'x', 'l', '{', '?', ')', 'H', '<', 'd', 'S', '0', '/', 't', '|', 'w', '7', '>', 'b', 'T', '$', 'O', '%', '!', 'L', 'n', '^', 'f', 'A', 'J', "'", '+', '}', '6', ',', '2', '*', 'a', 'j', 'Q', '`', '_', '\\', 'I', 'q', '@', 'i', 'R', 'v', '-', 'e', ']', 'u', ':', 'z', 'P', '~', '#', 'c', 'r', 'y', 'D', 'k', 'g', 'F', '9', 's', 'm', ';', 'E', 'W', 'o']
    },
    "c": {
      "notches": [True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, True, False, False, False, True],
      "wiring": ['b', '"', '!', '-', 'D', 'H', "'", '&', 'v', 'x', '`', 'M', 'B', '#', 'h', 'u', 'k', 'F', 'G', 'X', 'W', 'J', 'P', 'a', '_', ':', '9', 'Z', 'p', 'j', '{', '[', 'K', 'r', ',', 'd', '$', 'm', '1', '2', '%', 'y', '5', '@', '^', '+', 'n', 'e', '6', 'q', 'V', 'U', ']', 'S', 'R', '4', '3', '}', ';', '?', 't', 'T', 'L', '8', '*', '7', ' ', '~', 'C', 'O', 's', 'o', '.', 'w', '=', '0', 'z', 'E', 'N', 'g', '<', 'Q', 'A', 'f', '\\', '/', '(', 'i', ')', 'I', 'l', '>', '|', 'Y', 'c']
    },
    "d": {
      "notches": [True, True, True, False, True, False, False, False, True, False, True, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True],
      "wiring": ['Y', ',', 'n', 'I', '6', 'w', 'C', '{', '7', '_', 'g', 'o', '!', 'r', 'y', 'S', 'G', 'p', 'U', 't', '9', '5', '$', '(', 'Q', '4', 'E', 'd', 'h', 'A', ']', 'H', 'f', '=', 'j', '&', '~', ':', 'q', '0', '?', '#', 's', 'b', '|', 'x', 'Z', 'u', '^', '8', '\\', '/', 'c', '2', '`', 'z', '[', ' ', 'N', 'X', 'R', '>', 'P', ')', 'V', 'e', 'K', 'T', ';', 'a', '@', '*', '<', '}', 'B', 'l', 'k', 'v', '"', '+', '1', 'F', '-', 'J', '3', 'O', 'm', '%', 'M', '.', 'W', "'", 'L', 'i', 'D']
    },
    "e": {
      "notches": [True, True, True, False, True, True, False, True, True, False, False, True, False, True, False, True, False, False, False, True, True, False, True, True, False, True],
      "wiring": ['S', '[', 'J', 'Z', 'N', '+', 'n', 'i', 'd', 'B', '@', '%', 'K', 'f', 'j', ']', 'P', '>', 'm', 'U', '_', '\\', '|', 'D', 'G', 'o', 't', 'X', 'T', '}', '1', 'H', '*', 's', ')', 'a', '7', 'M', 'Q', '8', '?', 'q', '"', ',', 'k', 'E', '$', 'v', '0', 'F', 'c', ' ', '<', '3', 'r', 'Y', ';', 'W', '#', '!', '5', '/', 'u', '4', 'h', 'C', 'w', 'R', '(', 'y', '-', 'x', '`', "'", '.', 'L', 'l', '2', '&', '9', '{', 'I', 'V', 'A', ':', '^', 'O', 'b', 'g', 'e', '~', 'p', '6', '=', 'z']
    },
    "f": {
      "notches": [False, True, True, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, True],
      "wiring": ['R', 'e', ':', 'g', '(', 'H', '&', 'L', '$', 'Z', ';', '}', 'Y', '<', '|', 'c', '^', 'h', '?', '=', '@', 'F', 'w', 'f', 'M', 'a', '"', '*', '-', '3', 'Q', '2', '4', '_', 'u', ']', 'K', 'l', '5', 'z', '%', 'b', '{', 'D', "'", '8', 'd', '\\', '~', '>', ' ', 'p', 'V', 'r', 'T', 'n', '[', ',', ')', 'X', 'O', 'C', '0', 'A', 'j', '9', 'I', '/', 'N', '!', '7', '#', '1', 'x', '`', 'o', 'E', 's', 'W', 'k', 'S', 'y', 'U', 'm', 'v', 'B', 't', '6', 'i', 'q', 'G', 'J', '.', '+', 'P']
    },
    "g": {
      "notches": [True, True, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, False],
      "wiring": ['a', 'H', '?', '%', 'V', '#', 'K', 'O', 'u', '{', 'j', 'M', 'J', 'p', '4', 'U', ':', 'c', 'L', 'A', '.', 'q', 'g', 'x', 'Q', '|', '0', '~', '@', 'E', 'N', '"', '<', '3', 's', 'W', 'h', '=', 'Z', '}', '!', 'r', ',', '&', '2', '+', '>', "'", 'm', '8', 'i', 'y', 'd', '/', '$', 'C', 'b', 'z', 'F', '`', 'l', 'f', 'k', 'e', '[', ' ', 'X', '1', 'T', '_', ']', '6', 'D', 'R', '*', '^', '\\', 'P', 'w', 'o', '-', '5', 'I', 'B', 'v', '(', 't', 'n', '7', 'S', 'Y', ')', '9', 'G', ';']
    },
    "h": {
      "notches": [True, True, False, False, True, False, True, False, True, False, False, True, False, False, False, True, True, False, True, False, True, True, False, False, True, False],
      "wiring": ['I', '1', 'Z', 'F', 'w', '*', '.', 'p', 'c', 'S', '%', ';', 'h', 'N', '&', 'k', 'Y', '!', 'm', '[', 'x', 'H', 'M', 'a', '~', 'g', 'A', '+', '_', '@', 'z', 'j', '=', ':', 'y', '^', 'd', 'O', '#', 'i', '5', ' ', 'W', 'P', '|', '6', '-', 'E', 'K', 'l', 'T', ')', 'R', 'f', 'r', 'J', '\\', '0', '"', '3', 'X', '}', 'C', '<', 'b', '7', '`', '(', 'D', 'q', 'U', '9', ',', 'G', '?', '/', 'Q', '2', 'u', 'o', "'", 'e', 'V', 'v', '{', 'n', 's', '$', '4', 'B', '>', 't', 'L', ']', '8']
    },
    "i": {
      "notches": [True, False, True, False, False, False, True, False, False, False, False, False, False, True, True, True, True, False, True, False, False, True, True, False, True, True],
      "wiring": ['_', 'z', 'n', ':', '{', 'S', 'D', '0', '5', 'N', 'Q', 'J', 'b', 'I', 'r', '8', "'", 'q', 'K', 'f', 'm', '(', 'W', 'x', '/', 'e', '#', 'y', 'H', 'M', 'p', 'g', 'O', 'U', ']', 'l', '&', '~', 'G', 'F', '<', '-', '+', '2', 'j', '=', ')', '@', 'P', '*', '}', '%', 'X', 'A', 'w', '6', 'T', 'u', 'k', 'v', '|', 'B', 'o', ' ', 'c', 's', ',', '`', 't', '9', '3', '?', 'i', 'h', 'L', 'Z', 'C', '4', '"', '^', '>', '1', '.', 'a', 'd', 'Y', '[', 'V', '7', ';', '!', '$', '\\', 'R', 'E']
    },
    "j": {
      "notches": [True, True, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True],
      "wiring": ['j', 'm', '9', '6', 'W', 'r', 'c', 'U', '<', ')', 'i', '4', '8', '0', '1', 'E', '-', '.', '=', 'G', '+', 'p', '#', 'a', ',', '"', '?', 'o', '(', '2', 'x', ':', 'u', 'V', 'H', '`', 's', '/', 'R', '3', 'B', 't', '^', 'N', 'w', 'X', 'K', 'v', 'Z', 'k', 'F', 'q', '{', "'", 'A', '$', 'M', '}', 'P', 'e', 'l', 'g', 'J', 'n', 'C', '7', 'f', '&', 'z', '[', 'b', ']', '~', '*', ' ', 'Q', '\\', '!', '_', ';', '5', 'S', '%', 'D', 'I', '@', 'O', 'L', '>', '|', 'd', 'T', 'y', 'Y', 'h']
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

  # Generates the "wiring" for a rotor
  @staticmethod
  def create_rotor():
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

    # for i in range(len(Enigma.alphabet)):
    #   j = Enigma.get_rand_in_alphabet(chosen)
    #   chosen.append(j)
    #   wiring[i] = Enigma.alphabet[j]

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

    # Rotate the mechanism
    # self.rotate()

    char = self.plugboard[char] if char in self.plugboard else char
    
    return char

  def rotate(self):
    if Enigma.rotors[self.rotors[0]]["notches"][self.rotor_positions[0]]:
      if Enigma.rotors[self.rotors[1]]["notches"][self.rotor_positions[1]]:
        self.rotor_positions[2] = (self.rotor_positions[2] + 1) % len(Enigma.alphabet)
      
      self.rotor_positions[1] = (self.rotor_positions[1] + 1) % len(Enigma.alphabet)
    
    self.rotor_positions[0] = (self.rotor_positions[0] + 1) % len(Enigma.alphabet)

  def pass_through_rotor(self, char, index, rev=False):
    rotor = Enigma.rotors[self.rotors[index]]
    i = (Enigma.char_code(char) + self.rotor_positions[index]) % len(Enigma.alphabet)
    return Enigma.alphabet[rotor["wiring"].index(char)] if rev else rotor["wiring"][i]

enigma = Enigma()
print(enigma.encode("E"))

# print(Enigma.create_rotor())