import os
reader = open('euler11.txt')
file_lines = reader.readlines()
reader.close()

def right(lines, i, j):
    if j > 16:
        return 1
    else:
        return lines[i][j]*lines[i][j+1]*lines[i][j+2]*lines[i][j+3]

def down(lines, i, j):
    if i > 16:
        return 1
    else:
        return lines[i][j]*lines[i+1][j]*lines[i+2][j]*lines[i+3][j]

def rdiag(lines, i, j):
    if (i > 16) or (j > 16):
        return 1
    else:
        return lines[i][j]*lines[i+1][j+1]*lines[i+2][j+2]*lines[i+3][j+3]

def ldiag(lines, i, j):
    if (i > 16) or (j < 3):
        return 1
    else:
        return lines[i][j]*lines[i+1][j-1]*lines[i+2][j-2]*lines[i+3][j-3]

lines = []
for line in file_lines:
    lines.append( line.replace("\n","").split(" "))

for i in range(0,20):
    for j in range(0,20):
        lines[i][j] = int(lines[i][j])

max = (100, 1,1,"u")
for i in range(0,20):
    for j in range(0,20):
        r = right(lines,i,j)
        if r > max[0]:
            max = (r,i,j,"r")
        d = down(lines,i,j)
        if d > max[0]:
            max = (d,i,j,"d")
        rg = rdiag(lines,i,j)
        if rg > max[0]:
            max = (rg,i,j,"rg")
        lg = ldiag(lines,i,j)
        if lg > max[0]:
            max = (lg,i,j,"lg")
    
print(max)
