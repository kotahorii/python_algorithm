# subject_score = [70, 98, 92, 88, 64]
# total_score = 0
# average_score = 0

# for i, _ in enumerate(subject_score):
#     total_score += subject_score[i]
#     average_score = total_score / len(subject_score)

# print(total_score, average_score)

# sum = 0
# for i in range(1, 11):
#     sum += i

# print(sum)


# def sum_number(n: int) -> int:
#     total = 0

#     for i in range(1, n + 1):
#         total += i

#     return total


# print(sum_number(10))


# def sum_number(n: int) -> int:
#     total = (1 + n) * (n / 2)
#     return int(total)


# print(sum_number(9))

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
