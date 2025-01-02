a = list(map(int, open('17 (17).txt').readlines()))
s = []
for i in a:
    if i % 2 == 0:
        s.append(i)
sr = sum(s) / len(s)
m = []
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 and a[i + 1] < sr) or (a[i] < sr and a[i + 1] % 3 == 0):
        m.append(a[i] + a[i + 1])
print(len(m), max(m))