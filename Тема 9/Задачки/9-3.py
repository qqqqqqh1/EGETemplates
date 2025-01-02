f = open('9-3.txt')
k = 0   #11 22 33 44
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    s1 = a[2] * a[1]
    s2 = a[0] * a[3]
    if s1 == s2:
        if (a[-2] ** 2) > (a[0] * a[-1]):
            k += 1
print(k)
