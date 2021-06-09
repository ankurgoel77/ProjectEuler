# Find 10000 triangle, 10000 pent, and 10000 hex

high = 100000
tri_set = set()
pent_set = set()
hex_set = set()

for i in range(0,high):
    n = i+1
    tri_set.add(n*(n+1) // 2)
    pent_set.add(n*(3*n -1) // 2)
    hex_set.add( n*(2*n-1) )

for i in tri_set:
    if (i in pent_set) and (i in hex_set):
        print(i)