def step(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

max_count = (1,1)
for i in range(1,1000000):
    count = 1
    n = i
    while not n == 1:
        count += 1
        n = step(n)
    if count > max_count[0]:
        max_count = (count,i)

print(max_count)