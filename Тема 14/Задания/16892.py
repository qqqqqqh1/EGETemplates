def f(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x //= 5
    return(s)

a = 125 ** 4 + 25 ** 8 - 30
b = f(a)
print(b.count('4'))