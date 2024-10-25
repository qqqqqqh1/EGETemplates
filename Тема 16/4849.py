def f(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return f(n - 2) * n
print(f(7))