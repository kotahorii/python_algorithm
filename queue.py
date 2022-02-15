from collections import deque
from typing import Any


def reverse(queue: deque[Any]) -> deque[Any]:
    new_queue: deque[Any] = deque()
    while queue:
        new_queue.append(queue.pop())

    return new_queue


if __name__ == "__main__":
    que: deque[int] = deque()
    que.append(1)
    que.append(2)
    que.append(3)
    que.append(4)
    print(que)
    print(reverse(que))
