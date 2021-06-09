# def get_primes(n):
#     primes = []

#     while n % 2 == 0 :
#         primes.append(2)
#         n = n / 2

#     for i in range(3,int(n**0.5)+1,2):
#         while n % i == 0:
#             primes.append(i)
#             n = n / i
#     if n > 2 :
#         primes.append(int(n))
#     return primes

# for i in range (2,21):
#     print(get_primes(i))

# def divisible(n):
#     for i in range (1,21):
#         if not (n % i == 0):
#             return False
#     return True

# for i in range(2520,41902660800,20):
#     if divisible(i):
#         print(i)

def divisible(n):
    for i in range (11,21):
        if not (n % i == 0):
            return False
    return True

for i in range(2520,41902660800,20):
    if divisible(i):
        print(i)
