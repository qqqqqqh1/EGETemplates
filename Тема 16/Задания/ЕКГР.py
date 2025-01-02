from sys import *
from functools import *

setrecursionlimit(10 ** 9)
@lru_cache(None)

def f(n):
    if n < 6:
        return n
    if n >= 6:
        return 3 * n * f(n - 3)

print((f(12571) - 9 * f(21568)) / f(12565))