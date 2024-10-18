def f(num, base):
    return sum([num[i] * base ** i for i in range(len(num))])

for x in range(17):
    x1 = f([x, 11, 0, 9][::-1], 17)
    x2 = f([x, 8, 14, 8][::-1], 15)
    res = x1 + x2
    if res % 155 == 0:
        print(res // 155)