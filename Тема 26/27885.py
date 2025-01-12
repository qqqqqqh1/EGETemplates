s, n = 7718, 2810
f = list(map(int, open('27885.txt').readlines()[1:]))
m = 0
c = 0
f.sort()
for i in f:
    if m <= s:
        m += i
        c += 1
        print(i)
print(f[c])
print(m - 23, c - 1)
print(f[650])

