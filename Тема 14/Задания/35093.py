def f(n):
    a = ''
    while n > 0:
        a = str(n % 9) + a
        n //= 9
    return a
b = (729 ** 6) + (3 ** 14) - 36
print(f(b).count('0'))