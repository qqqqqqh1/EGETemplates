l = open('58328.txt').readline()
m = 0
cnt = 0
for i in range(len(l) - 1):
    if l[i] != l[i + 1]:
        cnt += 1
        m = max(cnt + 1, m)
    else:
        cnt = 0
print(m)
