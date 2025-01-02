f = list(map(int, open('17 (10).txt').readlines()))
mi = []
for i in range(len(f)):
    if f[i] % 19 == 0:
      mi.append(f[i])
mm = min(mi)
k = []
for j in range(len(f) - 1):
    if (f[j] < mm or f[j + 1] < mm):
        k.append(f[j] + f[j + 1])
print(len(k), max(k))