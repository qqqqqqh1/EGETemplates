f = open('пробник 27.01.txt')
k = 0
for s in f:
    a = [int(i) for i in s.split()]
    g = [a.count(x) for x in a]
    if g.count(1) == 4:
        if max(a) < (sum(a) - max(a)):
            k += 1
print(k)