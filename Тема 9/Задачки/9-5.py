f = open('9-5.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    p = [a.count(x) for x in a]
    if max(a) < (sum(a) - max(a)):
        if p.count(2) == 2:
            k += 1
print(k)