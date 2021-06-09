total = 0

for a in range (0,200):
    for b in range(0,100):
        for c in range(0,40):
            for d in range(0,20):
                for e in range(0,10):
                    for f in range(0,4):
                        for g in range(0,2):
                            if (1*a) + (2*b) + (5*c) + (10*d) + (20*e) + (50*f) + (100*g) == 200:
                                total += 1

print(total+8)