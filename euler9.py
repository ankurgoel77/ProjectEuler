for a in range(1,999):
    for b in range(1,999):
        c = (a**2 + b**2)**0.5
        if abs(1000-a-b-c) < 0.0005:
            print(a, b, c, a*b*c)
