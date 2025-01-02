f = open('9-7.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    sr1 = [x for x in a if a.count(x) == 1]
    sr2 = [x for x in a if a.count(x) > 1]
    if len(sr1) > 0 and len(sr2) > 0:
        if (sum(sr1) / len(sr1)) < (sum(sr2) / len(sr2)):
            k += 1
print(k)