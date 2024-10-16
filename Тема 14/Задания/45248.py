def f(num):
    a = ''
    while num > 0:
        a = str(num % 8) + a
        num //= 8
    return a

s = 7 * (512 ** 1912) + 6 * (64 **1954) - 5 * (8 **1991) - 4 * (8 **1980) - 2022
d = f(s)
print(d.count('7'))