with open('demo_2025_27_Б.txt') as f:
    f.readline()
    cl1, cl2, cl3 = [], [], []
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        if 0 <= x <= 2.5 and 0 <= y <= 3:
            cl1.append((x, y))
        if 2 <= x <= 4.5 and 6 <= y <= 11:
            cl2.append((x, y))
        if 5 <= x <= 8 and 4 <= y <= 7:
            cl3.append((x, y))

def f(cl):
    xc, yc, minim = 0, 0, 10 ** 100
    for i in range(len(cl)):
        res = 0
        for j in range(len(cl)):
            x1, y1 = cl[i]
            x2, y2 = cl[j]
            res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if res < minim:
            minim = res
            xc, yc = x1, y1
    return xc, yc

x1, y1 = f(cl1)
x2, y2 = f(cl2)
x3, y3 = f(cl3)
print(int((x1 + x2 + x3) / 3 * 10000), int((y1 + y2 + y3) / 3 * 10000))
