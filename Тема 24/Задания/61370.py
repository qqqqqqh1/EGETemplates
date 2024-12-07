f = open('61370.txt').readline()
m = 0
for i in range(len(f)):
    a, b, c = 0, 0, 0
    for p in range(i, len(f)):
        c += 1
        if f[p] == "B":
            b += 1
        if f[p] == "A":
            a += 1
        if a > 1 or b > 1:
            m = max(m, c - 1)
            break
print(m)