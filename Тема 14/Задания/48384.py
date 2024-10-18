def f(num, base):
    return sum([num[i] * base ** i for i in range(len(num))])

for x in range(11):
    for y in range(11):
        x1 = f([8, 8, x, 4, y][::-1], 9)
        x2 = f([7, x, 4, 4, y][::-1], 11)
        res = x1 + x2
        if res % 61 == 0:
            print(res // 61)
            break