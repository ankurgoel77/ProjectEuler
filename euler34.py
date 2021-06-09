import math

total = 0
for i in range(3,10000000):
    if sum([math.factorial(int(j)) for j in str(i)]) == i:
        total += i
        print(i)

print(f'Total: {total}')