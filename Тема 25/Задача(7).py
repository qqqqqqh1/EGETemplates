def f(x):
    a = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            a.append(i)
    if len(a) == 4:
        return a
for i in range(12345, 12446):
    if f(i):
        print(f(i))