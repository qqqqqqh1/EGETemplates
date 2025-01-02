f = list(map(int, open('задание 17.txt').readlines()))
m = min(f)
s = []
for i in range(len(f) - 1):
    if f[i] % 22 == m or f[i + 1] % 22 == m:
        s.append(f[i] + f[i + 1])
print(len(s), max(s))