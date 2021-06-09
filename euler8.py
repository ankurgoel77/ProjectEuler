import os
reader = open('euler8.txt')
file_lines = reader.readlines()
reader.close()

def prod(iter):
    total = 1
    for i in iter:
        total *= i
    return total

digit_list = []
for line in file_lines:
    for digit in list(line):
        if digit.isdigit():
            digit_list.append(int(digit))

max = 0
for i in range(0,988):
    test = prod(digit_list[i:i+13])
    if test > max:
        max = test
print(max)
