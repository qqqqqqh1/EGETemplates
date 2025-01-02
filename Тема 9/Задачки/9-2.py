f = open('9-2.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if max(a) < (sum(a) - max(a)):
        if (a[0] + a[-1]) == (a[1] + a[2]):
            k += 1
print(k)