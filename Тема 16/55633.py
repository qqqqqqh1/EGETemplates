import sys
sys.setrecursionlimit(10000)
def f(a, b):
    if b == 0:
        return a
    elif a >= b > 0:
        return f(a-b, b)
    elif a < b:
        return f(b, a)
count = 0
for i in range(123456798, 1234567886):
    if f(i, 15) == 15:
        count += 1
print(count)