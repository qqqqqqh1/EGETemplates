"""
Алгоритм вычисления значения функции F(n), где n — целое число, задан следующими соотношениями:

F(n) = n, если n < 10
F(n) = F(n mod 10) + F(n div 10), если n >= 10.

Определите количество значений n, меньших 2^63, для которых F(n) = 159.

Ответ: 34602572
"""
from functools import cache

"""
from functools import *

# граничное значение
a = list(map(int, str(2 ** 63 - 1)))


@cache
def f(s, l, fl):
    if l == 0:
        return s == 159
    # проверяем ограниченные подпоследовательности большей длины
    return sum(f(s + x, l - 1, fl and (x == a[-l])) for x in range([10, a[-l] + 1][fl]))

print(f(0, len(a), 1))
"""

"""
def f(n):
    if n < 10:
        return n
    else:
        return f(n % 10) + f(n // 10)


count = 0
for n in range(2 ** 63 - 1):
    if f(n) == 159:
        count += 1
print(count)
"""