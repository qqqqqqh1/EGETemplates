f = open('9-4.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    p = [a.count(x) for x in a]
    if max(a) > (sum(a) - max(a)):
        if p.count(1) == 4:
            k += 1
print(k)

