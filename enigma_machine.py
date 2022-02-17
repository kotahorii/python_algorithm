import random
import string

ALPHABET = string.ascii_uppercase


class PlugBoard:
    def __init__(self, map_alphabet: str) -> None:
        self.alphabet = ALPHABET
        self.forward_map = {}
        self.backword_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet: str):
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        self.backword_map = {v: k for k, v in self.forward_map.items()}

    def forward(self, index_num: int) -> int:
        char = self.alphabet[index_num]
        char = self.forward_map[char]
        return self.alphabet.index(char)

    def backword(self, index_num: int) -> int:
        char = self.alphabet[index_num]
        char = self.backword_map[char]
        return self.alphabet.index(char)


class Rotor(PlugBoard):
    def __init__(self, map_alphabet: str, offset=0) -> None:
        super().__init__(map_alphabet)
        self.offset = offset
        self.rotations = 0

    def rotate(self, offset=None):
        if not offset:
            offset = self.offset
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        return self.rotations

    def reset(self):
        self.rotations = 0
        self.alphabet = ALPHABET


class Reflector:
    def __init__(self, map_alphabet: str) -> None:
        self.map = dict(zip(ALPHABET, map_alphabet))
        for x, y in self.map.items():
            if x != self.map[y]:
                raise ValueError(x, y)

    def reflect(self, index_num: int):
        reflected_char = self.map[ALPHABET[index_num]]
        return ALPHABET.index(reflected_char)


class EnigmaMachine:
    def __init__(
        self, plug_board: PlugBoard, rotors: list[Rotor], reflector: Reflector
    ) -> None:
        self.plug_board = plug_board
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, text: str):
        return "".join([self.go_through(c) for c in list(text)])

    def decrypt(self, text: str):
        for rotor in self.rotors:
            rotor.reset()
        return "".join([self.go_through(c) for c in list(text)])

    def go_through(self, char: str) -> str:
        char = char.upper()
        if char not in ALPHABET:
            return char

        index_num = ALPHABET.index(char)
        index_num = self.plug_board.forward(index_num)

        for rotor in self.rotors:
            index_num = rotor.forward(index_num)

        index_num = self.reflector.reflect(index_num)

        for rotor in reversed(self.rotors):
            index_num = rotor.backword(index_num)

        index_num = self.plug_board.backword(index_num)
        char = ALPHABET[index_num]

        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return char


if __name__ == "__main__":

    def get_random_alphabet():
        return "".join(random.sample(ALPHABET, len(ALPHABET)))

    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 3)

    r = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes) / 2)):
        x = indexes.pop(random.randint(0, len(indexes) - 1))
        y = indexes.pop(random.randint(0, len(indexes) - 1))
        r[x], r[y] = r[y], r[x]
    reflector = Reflector("".join(r))

    machine = EnigmaMachine(p, [r1, r2, r3], reflector)

    s = "ATTACK SILICON VALLEY"
    e = machine.encrypt(s)
    print(e)
    d = machine.decrypt(e)
    print(d)
