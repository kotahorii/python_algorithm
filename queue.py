from collections import deque
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.queque: list[Any] = []

    def enqueue(self, data: Any) -> None:
        self.queque.append(data)

    def dequeue(self) -> Any:
        if self.queque:
            return self.queque.pop(0)


if __name__ == "__main__":
    que: deque[int] = deque()
    que.append(1)
    que.append(2)
    que.append(3)
    que.append(4)
    print(que)
    print(que.popleft())
