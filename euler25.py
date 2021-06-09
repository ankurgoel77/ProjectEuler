
f1 = 1
f2 = 1
i=2

while True:
    i += 1
    f = f1 + f2
    f2 = f1
    f1 = f
    if len(str(f)) > 999:
        print(i)
        break