def func2(n: float) -> None:
    if n <= 1:
        return
    else:
        print(n)
        func2(n / 2)


def func3(numbers: list[int]) -> None:
    for num in numbers:
        print(num)


def func4(n: float):
    for i in range(int(n)):
        print(i, end=" ")
    print()

    if n <= 1:
        return
    func4(n / 2)


def func5(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


func5([1, 2, 3, 4, 5])
