s = open('37159.txt').readline()
cnt = 0
m = 0
for i in range(len(s) - 1):
    if (s[i] == 'd' and s[i + 1] == 'a') or (s[i] == 'a' and s[i + 1] == 'd'):
        m = max(cnt + 1, m)
        cnt = 0
    else:
        cnt += 1
print(m)
