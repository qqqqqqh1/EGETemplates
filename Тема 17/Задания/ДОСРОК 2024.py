f = list(map(int, open('ДОСРОК 2024.txt').readlines()))
m = []
a = []
for i in f:
    if i % 19 == 0:
        m.append(i)
mm = min(m)
for i in range(len(f) - 1):
    if f[i] % mm == 0 or f[i + 1] % mm == 0:
        a.append(f[i] + f[i + 1])
print(len(a), max(a))
