nums = [0]*2000001

for i in range(2,1414):
    if nums[i] == 0:  #We found a prime
        for j in range(i*i,2000000,i):
            nums[j] = 1

primes = [i for i in range(2,2000000) if nums[i] == 0]


# total = 0
# for i in range(2,2000000):
#     if nums[i] == 0:
#         total += i

print(sum(primes))
