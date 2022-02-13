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

# for i in range(1, 10):
#     calc_results = ""
#     for j in range(1, 10):
#         calc_results += f"{j} * {i} = {i*j:2d}, "

#     print(calc_results)

# for devidend in range(2, 101):
#     max_range = devidend // 2
#     is_prime_number = True

#     for devisor in range(2, max_range + 1):
#         if devidend % devisor == 0:
#             is_prime_number = False
#             break

#     if is_prime_number:
#         print(devidend)

# factorial_num = 1
# for i in range(1, 11):
#     factorial_num *= i

# print(factorial_num)


# def culc_factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     return n * culc_factorial(n - 1)


# for i in range(21):
#     print(culc_factorial(i))

# num_list = [10, -5, 0, 29, 6, 2, 77, 8]

# for num in num_list:
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# n = range(1, 6)

# for i in n:
#     print(3 ** i - 2 ** i)


# p = [True] * 100
# p[0] = False
# p[1] = False
# n = 2


# def hyou() -> None:
#     s = ""
#     for i in range(100):
#         if p[i]:
#             s += f"{i:2d}, "
#         else:
#             s += " /, "
#         if i % 10 == 9:
#             s += "\n"
#     print(s)


# def furui() -> None:
#     global n
#     for i in range(n + n, 100, n):
#         p[i] = False
#     print(n, "の倍数をふるい落としました。")
#     hyou()
#     while n < 100:
#         n += 1
#         if p[n]:
#             break


# hyou()
# while n < 10:
#     input("Enterキーを押してください")
#     furui()
