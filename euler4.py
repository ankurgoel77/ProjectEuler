largest = 1
for i in range(101,1000):
    for j in range(101,1000):
        string = str(i*j)
        if string == string[::-1]:
            if i*j > largest:
                largest = i*j

print(largest)