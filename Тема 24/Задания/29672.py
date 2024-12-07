f = open('29672.txt').readlines()
c = 0
for i in range(len(f)):
    if f[i].count('E') > f[i].count('A'):
        c += 1
print(c)
