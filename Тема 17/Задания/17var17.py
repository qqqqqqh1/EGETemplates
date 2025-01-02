a = list(map(int, open('17var17.txt').readlines()))
m = []
j = []
for i in range(len(a) - 1):
    if (a[i] ** 2 + a[i + 1] ** 2) % 2 != 0 and (a[i] ** 2 + a[i + 1] ** 2) > 90:
        m.append(a[i] + a[i + 1])
        j.append(a[i])
        j.append(a[i + 1])
print(len(m))

