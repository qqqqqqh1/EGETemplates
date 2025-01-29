def f(x):
    a = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            a.append(i)
    if 41 <= len(a) <= 45:
        return len(a)

for i in range(3954, 8980):
    if f(i):
        print(i, f(i))