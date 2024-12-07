f = open('61404.txt').readline()
m = 0
for i in range(len(f)):
    cnt = 0
    x = 0
    y = 0
    for j in range(i, len(f)):
        cnt += 1
        if f[j] == 'X':
            x += 1
        if f[j] == 'Y':
            y += 1
        if x > 1 or y > 1:
            m = max(m, cnt - 1)
            break
print(m)