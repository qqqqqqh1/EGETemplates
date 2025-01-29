def f(x):
    a = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            a.append(i)
    if len(a) == 3:
        return max(a)

for i in range(123456789, 223456789):
    if f(i):
        print(i, f(i))