def get_pair(numbers: list[int], target: int):
    cache: set[int] = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return (val, num)
        cache.add(num)


def get_pair_half_sum(numbers: list[int]):
    sum_numbers = sum(numbers)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return

    return get_pair(numbers, half_sum)


if __name__ == "__main__":
    nums = [11, 2, 5, 9, 10, 3]
    print(get_pair(nums, 12))
    print(get_pair_half_sum(nums))
