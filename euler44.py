#find the first 100 pentagonal numbers
high = 10000
pent_list = [0]*high
for i in range(0,high):
    n = i+1
    pent_list[i] = n*(3*n -1) // 2

pent_set = set(pent_list)

for i in range(0,high):
    for j in range(0,high):
        if (pent_list[i] + pent_list[j]) in pent_set:
            if abs(pent_list[i] - pent_list[j]) in pent_set:
                print(i,j, pent_list[i], pent_list[j])