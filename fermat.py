import sys


def fermat_last_theorem_v1(max_num: int, squire_num: int) -> list[tuple[int, int, int]]:
    result = []
    if squire_num < 2:
        return result

    max_z = int(pow((max_num - 1) ** 2 + max_num ** 2, 1.0 / squire_num))
    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            for z in range(y + 1, max_z):
                if pow(x, squire_num) + pow(y, squire_num) == pow(z, squire_num):
                    result.append((x, y, z))
    return result


def fermat_last_theorem_v2(max_num: int, squire_num: int) -> list[tuple[int, int, int]]:
    result = []
    if squire_num < 2:
        return result

    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            pow_sum = pow(x, squire_num) + pow(y, squire_num)
            if pow_sum > sys.maxsize:
                raise ValueError(x, y, squire_num, pow_sum)
            z = pow(pow_sum, 1.0 / squire_num)
            if not z.is_integer():
                continue
            z = int(z)
            z_pow = pow(z, squire_num)
            if z_pow == pow_sum:
                result.append((x, y, z))
    return result


if __name__ == "__main__":
    print(fermat_last_theorem_v2(20, 2))
