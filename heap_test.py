import heapq
from collections import Counter


def top_n_with_heap(words: list[str], n: int) -> list[str]:
    counter_word = Counter(words)
    data = [(-counter_word[word], word) for word in counter_word]
    return [heapq.heappop(data)[1] for _ in range(n)]


if __name__ == "__main__":
    words = ["python", "c", "java", "go", "python", "c", "go", "python"]
    print(top_n_with_heap(words, 3))
