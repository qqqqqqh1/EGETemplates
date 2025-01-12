f = open('9.1.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    tr = [x for x in a if a.count(x) == 3]
    s1 = [x for x in a if a.count(x) == 1]
    if len(tr) == 3 and len(s1) == 3:
        if sum(tr) > sum(s1):
            k += 1
print(k)