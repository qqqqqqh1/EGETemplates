f = open('9z.txt')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    pov = [x for x in a if a.count(x) == 2]
    nepov = [x for x in a if a.count(x) == 1]
    if len(pov) == 4 and len(nepov) == 3:
        if sum(nepov) / 3 < sum(pov) / 4:
            c += 1
print(c)
