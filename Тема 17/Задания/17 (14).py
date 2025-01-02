a = list(map(int, open('17 (14).txt').readlines()))
m = []
for i in range(len(a) - 1):
    if a[i] % 5 == 0 and a[i + 1] % 5 == 0:
        m.append(a[i] + a[i + 1])
print(len(m), max(m))