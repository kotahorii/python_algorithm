import random

total = 0

for i in range(5):
    if i == 4:
        total *= 2
    else:
        total += i

print(total)
total *= 2


for i in range(10):
    r = random.randint(0, 10)
    print(r)
