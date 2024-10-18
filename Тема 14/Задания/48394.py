def f(num, base):
    return sum([num[i] * base ** i for i in range(len(num))])

for x in range(16):
    x1 = f([8, x, 8, 3, 4][::-1], 16)
    x2 = f([4, 4, x, 2, 7][::-1], 16)
    res = x1 + x2
    if res % 23 == 0:
        print(res // 23)