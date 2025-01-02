f = open('9-8.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    p = [a.count(x) for x in a]
    pov = [x for x in a if a.count(x) == 2]
    if len(set(pov)) == 2 and p.count(1) == 3:
        if (sum(pov) / len(pov)) < (sum(a) / len(a)):
            k += 1
print(k)