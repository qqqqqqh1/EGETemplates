from itertools import product
count = 0
for i in product('ГЕПАРД', repeat=5):
    i = ''.join(i)
    if i.count('Г') == 1 and i[0] != 'А' and i[-1] != 'Е':
        count += 1
print(count)