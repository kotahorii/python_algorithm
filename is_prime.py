import math


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


def is_prime_v4(num: int) -> bool:
    if num <= 1:
        return False
    if num < 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime_v4(97))
