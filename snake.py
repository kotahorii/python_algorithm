import operator


def snake_string_v1(chars: str) -> list[list[str]]:
    result: list[list[str]] = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


def snake_string_v2(chars: str, depth: int) -> list[list[str]]:
    result: list[list[str]] = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    op = operator.neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)
    return result


if __name__ == "__main__":
    numbers = [str(i) for _ in range(10) for i in range(10)]
    for line in snake_string_v2("".join(numbers), 5):
        print("".join(line))
