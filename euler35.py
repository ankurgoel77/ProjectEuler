import collections

def psieve():
    import itertools
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step

p = psieve()
primes = set()

for i in range(0,1000000):
    j = next(p)
    if j > 1000000:
        break
    primes.add(j)

primes_rot = set()
for num in primes:
    if num < 10:
        primes_rot.add(num)
    else:
        is_rot = True
        nstr = collections.deque(str(num))
        for i in range(1,len(nstr)):
            nstr.rotate(1)
            if not int("".join(nstr)) in primes:
                is_rot = False
        if is_rot:
            primes_rot.add(num)


print(len(primes_rot))