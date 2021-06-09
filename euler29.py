set_ab = set()

for i in range(2,101):
    for j in range(2,101):
        set_ab.add(i**j)

print(len(set_ab))