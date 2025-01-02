f = open('9-9.txt')
k = 0
for s in f:
    k += 1
    a = [int(x) for x in s.split()]
    sr2 = [x for x in a if a.count(x) == 2]
    sr = [x for x in a if a.count(x) == 1]
    if len(sr2) == 2 and len(sr) == 4:
        if sr2[0] >= (sum(sr) / 4):
            print(k)
            break
