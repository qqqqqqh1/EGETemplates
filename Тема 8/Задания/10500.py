from itertools import *
count = 0
for i in product('12345', repeat=5):
    p = ''.join(i)
    if p.count('1') == 3:
        count += 1
print(count)