from itertools import permutations

def isprime(n):
    primes = []

    while n % 2 == 0 :
        primes.append(2)
        n = n / 2

    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            primes.append(i)
            n = n / i

    if len(primes) > 0:
        return False
    else:
        return True
    return True




p = permutations("1234567", 7)

max_prime = 0

count = 0
for x in p:
    num = int( "".join(x))
    count += 1
    if isprime(num) and num > max_prime:
        max_prime = num

print(max_prime, count)
