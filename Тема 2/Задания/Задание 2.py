'''
from itertools import permutations, product

def f(x, y, z, w):
    return ((x == y) <= ((not(z)) or w)) == (not((w <= x) or (y <= z)))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    table = [
        (0, 1, x1, x2, 1),
        (x3, x4, 1, 0, 1),
        (0, x5, 0, 0, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, s))) == s[-1] for s in table):
                print(*p)
'''
print('wzyx')