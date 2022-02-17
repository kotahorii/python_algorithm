import string
from typing import Generator


def caesar_cipher(text: str, shift: int) -> str:
    result: str = ""
    len_alphabet = ord("Z") - ord("A") + 1
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - ord("A")) % len_alphabet + ord("A"))
        elif char.islower():
            result += chr((ord(char) + shift - ord("a")) % len_alphabet + ord("a"))
    return result


def caesar_cipher_hack(text: str) -> Generator[tuple[int, str], None, None]:
    len_alphabet = ord("Z") - ord("A") + 1
    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            if char.isupper():
                index = ord(char) - candidate_shift
                if index < ord("A"):
                    index += len_alphabet
                reverted += chr(index)
            elif char.islower():
                index = ord(char) - candidate_shift
                if index < ord("a"):
                    index += len_alphabet
                reverted += chr(index)
            else:
                reverted += char

        yield candidate_shift, reverted


if __name__ == "__main__":
    e = caesar_cipher("z", 3)
    print(e)
    for shift_num, decrypted in caesar_cipher_hack(e):
        print(f"{shift_num:2d}", decrypted)
