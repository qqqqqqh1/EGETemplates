from itertools import *
count = 1
for i in product('АКЛОШ', repeat=5):
    p = ''.join(i)
    if p == 'ШКОЛА':
        break
    count += 1
print(count)