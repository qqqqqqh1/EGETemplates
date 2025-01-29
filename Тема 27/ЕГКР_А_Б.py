cl1 = [[], []]
cl2 = [[], [], []]
for line in open('ЕКГР_A.txt'):
    x, y = [float(k) for k in line.split()]
    if y < -16/9 * x:
        cl1[0].append([x, y])
    else:
        cl1[1].append([x, y])

for line in open('ЕКГР_Б.txt'):
    x, y = [float(k) for k in line.split()]
    if x < 0:
        cl2[0].append([x, y])
    elif y < 7 and x > 0:
        cl2[1].append([x, y])
    elif y > 7 and x > 0:
        cl2[2].append([x, y])

def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def c(cl):
    m = []
    for t in cl:
        s = sum(d(t, t1) for t1 in cl)
        m.append([s, t])
    return min(m)[1]

cA = [c(cl) for cl in cl1]
cB = [c(cl) for cl in cl2]
pxA = abs(int(sum(x for x, y in cA) / 2 * 10000))
pyA = int(sum(y for x, y in cA) / 2 * 10000)
pxB = int(sum(x for x, y in cB) / 3 * 10000)
pyB = int(sum(y for x, y in cB) / 3 * 10000)
print(f'A: {pxA} {pyA}')
print(f'B: {pxB} {pyB}')