from typing import NewType

PhoneAlphabet = NewType("PhoneAlphabet", str)

NUM_ALPHABET_MAPPING = {
    0: PhoneAlphabet("+"),
    1: PhoneAlphabet("@"),
    2: PhoneAlphabet("ABC"),
    3: PhoneAlphabet("DEF"),
    4: PhoneAlphabet("GHI"),
    5: PhoneAlphabet("JKL"),
    6: PhoneAlphabet("MNO"),
    7: PhoneAlphabet("PQRS"),
    8: PhoneAlphabet("TUV"),
    9: PhoneAlphabet("WXYZ"),
}


def phone_memonic_v1(phone_number: str) -> list[PhoneAlphabet]:
    phone_number_list: list[int] = [int(s) for s in phone_number.replace("-", "")]
    candidate: list[PhoneAlphabet] = []
    tmp: list[PhoneAlphabet | str] = [""] * len(phone_number_list)

    def find_cadidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number_list):
            candidate.append("".join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number_list[digit]]:
                tmp[digit] = char
                find_cadidate_alphabet(digit + 1)

    find_cadidate_alphabet()
    return candidate


def phone_memonic_v2(phone_number: str) -> list[PhoneAlphabet]:
    phone_number_list = [int(s) for s in phone_number.replace("-", "")]
    candidate: list[PhoneAlphabet] = []
    stack: list[PhoneAlphabet] = [""]

    while len(stack) != 0:
        alphabets = stack.pop()
        if len(alphabets) == len(phone_number_list):
            candidate.append(alphabets)
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number_list[len(alphabets)]]:
                stack.append(alphabets + char)
    return candidate


if __name__ == "__main__":
    for s in phone_memonic_v2("568-379-8466"):
        if "LOVEPYTHON" in s:
            print(s)
