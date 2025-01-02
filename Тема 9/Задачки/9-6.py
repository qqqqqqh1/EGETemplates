f = open('9-6.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    p = [a.count(x) for x in a]
    d = [x for x in a if a.count(x) > 1]
    g = [x for x in a if a.count(x) == 1]
    if p.count(2) == 4 and p.count(1) == 2:
        if sum(set(d)) > sum(g):
            k += 1
print(k)