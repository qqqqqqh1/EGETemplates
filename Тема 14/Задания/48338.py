def f(num, base):
    return sum([num[i] * base ** i for i in range(len(num))])

for x in range(15):
    x1 = f([1, x, 5, 6, 3][::-1], 14)
    x2 = f([8, 7, 1, x, 3][::-1], 14)
    res = x1 + x2
    if res % 24 == 0:
        print(res // 24)
        break