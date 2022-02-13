import random


def in_order(numbers: list[int]) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def bogo_sort(numbers: list[int]):
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    print(bogo_sort([1, 5, 3, 2, 6]))
