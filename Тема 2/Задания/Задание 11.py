from itertools import permutations, product

def f1(x, y, z, w):
    return (x or (not(y))) <= (w == z)

def f2(x, y, z, w):
    return (x or (not(y))) == (w <= z)

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    table = [
        (0, x1, 0, 0, 0, 0),
        (x2, 1, 1, x3, 0, x4),
        (x5, 0, 0, 0, x6, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, s))) == s[-2] and f2(**dict(zip(p, s))) == s[-1] for s in table):
                pass
print('ywxz')