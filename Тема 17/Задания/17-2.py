a = list(map(int, open('17-2.txt').readlines()))
m = []
j = []
for i in range(len(a) - 1):
    if (abs(a[i]) % 10 == 7 and abs(a[i]) % 3 == 0) or (abs(a[i + 1]) % 3 == 0 and abs(a[i + 1]) % 10 == 7):
        m.append(a[i] + a[i + 1])
        j.append(a[i])
        j.append(a[i + 1])
print(len(m), min(j))