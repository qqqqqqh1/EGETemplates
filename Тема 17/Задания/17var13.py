a = list(map(int, open('17var13.txt').readlines()))
m = []
for i in range(len(a) - 1):
    if a[i] < 450 and a[i + 1] < 450:
        m.append(a[i] ** 3 + a[i + 1] ** 3)
print(len(m), max(m))