from itertools import *
count = 0
for i in permutations('МАТВЕЙ'):
    p = ''.join(i)
    if p[0] != 'Й' and p.count('АЕ') == 0:
        count += 1
print(count)