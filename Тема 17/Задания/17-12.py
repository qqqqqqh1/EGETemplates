a = list(map(int, open('17-12.txt').readlines()))
m = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] % 3 == 0 or a[j] % 3 == 0:
            m.append(a[i] + a[j])
print(len(m), max(m))