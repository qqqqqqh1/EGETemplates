def f(n):
    a = ''
    while n > 0:
        a = str(n % 7) + a
        n //= 7
    return a

for x in range(2031):
    if f(7 ** 170 + 7 ** 100 - x).count('0') == 71:
        print(x)