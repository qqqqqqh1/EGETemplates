from itertools import *
count = 1
for i in product('АОУ',repeat=5):
    p = ''.join(i)
    if p == 'УАУАУ':
        break
    count += 1
print(count)