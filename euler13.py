import os
reader = open('euler13.txt')
file_lines = reader.readlines()
reader.close()

num = 0
for line in file_lines:
    num += int(line.replace("\n",""))

print(num)