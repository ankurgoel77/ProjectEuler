def get_primes(n):
    primes = []

    while n % 2 == 0 :
        primes.append(2)
        n = n / 2

    for i in range(3,int(n**0.5)+1,2):
        while n % i == 0:
            primes.append(i)
            n = n / i
    if n > 2 :
        primes.append(int(n))
    return primes

print(get_primes(600851475143))