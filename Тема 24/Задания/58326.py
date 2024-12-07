f = open('58326.txt').readline()
c = 1
m = 0
for i in range(len(f) - 1):
    if f[i] > f[i + 1]:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)