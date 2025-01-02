from itertools import *
f = open('24.6.txt').readline() # NOP NPO ONP OPN PNO PON
                                #     NPO         PNO
c = 0
m = 0
for i in range(0, len(f) - 2, 3):
    if f[i] + f[i + 1] + f[i + 2] == 'NPO' or f[i] + f[i + 1] + f[i + 2] == 'PNO':
        c += 1
        m = max(c, m)
    else:
        c = 0
print(m)
