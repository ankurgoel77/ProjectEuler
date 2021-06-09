def value(word):
    total = 0
    for letter in word:
        total += ord(letter) - 64
    return total

#generate the first 50 triangle numbers
triangles = set()
for i in range(1,51):
    t = i*(i+1) // 2
    triangles.add(t)

import os
reader = open('p042_words.txt')
file_lines = reader.readlines()
reader.close()

total = 0
for line in file_lines:
    words = line.split(",")
    for rawword in words:
        word = rawword.replace('"','')
        if value(word) in triangles:
            total += 1

print(total)
    
