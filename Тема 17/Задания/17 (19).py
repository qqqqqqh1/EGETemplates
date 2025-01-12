a = list(map(int, open('17 (19).txt').readlines()))
f = []
for i in range(len(a) - 1):
    if (a[i] * a[i + 1]) % 15 == 0 and (a[i] + a[i + 1]) % 7 == 0:
        f.append(a[i] + a[i + 1])
print(len(f), max(f))