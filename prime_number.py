from typing import Generator


def generate_primes_v1(number: int) -> list[int]:
    primes: list[int] = []
    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes


def generate_primes_v2(number: int) -> Generator[int, None, None]:
    cache: dict[int, bool] = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        cache[x] = True
        for y in range(x * 2, number + 1, x):
            cache[y] = False


if __name__ == "__main__":
    print([s for s in generate_primes_v2(50)])
