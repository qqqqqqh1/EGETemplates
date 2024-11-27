l = open('27688.txt').readline()
m = 0
cnt = 0
for i in range(len(l) - 1):
    if (l[i] == 'Z' and l[i + 1] == 'Z'):
        cnt += 1
        m = max(cnt + 1, m)
    else:
        cnt = 0
print(m)