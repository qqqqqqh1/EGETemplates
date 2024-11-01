import sys

sys.setrecursionlimit(10000)
def f(a, b):
    if b == 0:
        return a
    elif a >= b > 0:
        return f(a - b, b)
    elif a < b:
        return f(b, a)


x = 123456810
count = 6
while x < 1234567885:
    count += 8
    x += 15
print(x)
print(count - 3)