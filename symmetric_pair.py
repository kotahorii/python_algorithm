def find_pair(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    d: dict[int, int] = {}
    output: list[tuple[int, int]] = []
    for pair in pairs:
        if pair[1] in d and pair[0] in d.values():
            output.append(pair)
        else:
            d[pair[0]] = pair[1]
    print(d)
    return output


if __name__ == "__main__":
    num_list = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    print(find_pair(num_list))
