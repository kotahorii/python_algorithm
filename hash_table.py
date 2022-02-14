import hashlib
from typing import Any

TableType = list[list[list[str]]]


class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table: TableType = [[] for _ in range(self.size)]

    def hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: str, value: str) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")
            print()

    def get(self, key: str) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key: str, value: str) -> None:
        self.add(key, value)

    def __getitem__(self, key: str) -> Any:
        return self.get(key)


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table["car"] = "Tesla"
    hash_table["sns"] = "Youtube"
    hash_table.print()
    print(hash_table["sns"])
