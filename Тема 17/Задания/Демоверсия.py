f = list(map(int, open('Демоверсия.txt').readlines()))
m = min(f)
k = []
for i in range(len(f) - 1):
    if f[i] % 16 == m or f[i + 1] % 16 == m:
        k.append(f[i] + f[i + 1])
print(len(k), max(k))