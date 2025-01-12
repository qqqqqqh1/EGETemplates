f = open('пробник.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    pov = [x for x in a if a.count(x) == 1]
    nepov = [x for x in a if a.count(x) > 1]
    if len(pov) != 0 and len(nepov) != 0:
        if (sum(pov) / len(pov)) < (sum(nepov) / len(nepov)):
            k += 1
print(k)