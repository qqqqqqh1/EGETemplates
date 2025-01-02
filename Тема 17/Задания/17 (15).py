a = list(map(int, open('17 (15).txt').readlines()))
j = []
for i in a:
    if i % 2 == 0:
        j.append(i)
m = []
mi = sum(j) / len(j)
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (a[i] < mi or a[i + 1] < mi):
        m.append(a[i] + a[i + 1])
print(len(m), max(m))