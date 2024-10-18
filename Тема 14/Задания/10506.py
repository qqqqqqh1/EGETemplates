def f(n):
    a = ''
    while n > 0:
        a = str(n % 4) + a
        n //= 4
    return a

print(f((16 ** 2016) + (4 ** 2015) - 64).count('3'))