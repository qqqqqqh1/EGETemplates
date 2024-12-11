from itertools import permutations, product

def f(x, y, z, w):
    return (not(y)) and x and ((not(z)) or w)

for x1 in product([0, 1], repeat=1):
    table = [
        (0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 0, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, s))) == s[-1] for s in table):
                print(*p)