f = open('27694.txt').readline()
f = f.replace('AB', '*')
c = 0
m = 0
for i in range(len(f) - 1):
    if f[i] == '*':
        c += 2
    else:
        m = max(m, c)
        c = 0
print(m)