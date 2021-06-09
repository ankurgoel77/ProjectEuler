import os
reader = open('p067_triangle.txt')
file_lines = reader.readlines()
reader.close()

lines = []
for line in file_lines:
    line1 = line.replace("\n","")
    lines.append([int(i) for i in line1.split(" ")])

num_rows = len(lines)

sums = []
for i in range(0,num_rows):
    sums.append([0]*(i+1))

sums[0][0] = lines[0][0]
for i in range(1,num_rows):
    sums[i][0] = sums[i-1][0] + lines[i][0]
    sums[i][i] = sums[i-1][i-1] + lines[i][i]

for i in range(2, num_rows):
    for j in range(1,i):
        sums[i][j] = lines[i][j] + max(sums[i-1][j-1],sums[i-1][j])



print(max(sums[num_rows-1]))
