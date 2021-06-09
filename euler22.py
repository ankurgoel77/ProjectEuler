def value(name):
    total = 0
    for letter in name:
        total += (ord(letter) - 64)
    return total

reader = open('p022_names.txt')
file_lines = reader.readlines()
reader.close()


names = []
for line in file_lines:
    words = line.split(",")
    for rawword in words:
        word = rawword.replace('"','')
        names.append(word)
names.sort()

total = 0
for i in range(1,len(names)+1):
    total += i * value(names[i-1])

print(total)