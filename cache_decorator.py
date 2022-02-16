import time
from typing import Any, Callable


def memoize(f: Callable[[int], Any]):
    cache: dict[int, Callable[[int], Any]] = {}

    def _wrapper(n: int):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper


@memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(1000000):
        r += num * i
    return r


if __name__ == "__main__":
    for i in range(10):
        print(long_func(i))

    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)
