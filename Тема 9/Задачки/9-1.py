f = open('9-1.txt')
k = 0        # 11 22 33 44
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if max(a) < (sum(a) - max(a)):
        if a[0] + a[-1] != a[2] + a[1]:
            k += 1
print(k)
