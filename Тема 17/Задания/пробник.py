f = list(map(int, open('пробник.txt').readlines()))
def f1(x, y):
    m = [len(str(x)), len(str(y))]
    if m.count(4) == 1:
        return True
def f2(x, y, m):
    s = (x ** 2 + y ** 2)
    if s % m == 0:
        return True

def f3(x):
    m = [len(str(x))]
    if m.count(3) == 1:
        return True

s = []
for i in range(len(f)):
    if f3(f[i]) and f[i] % 10 == 5:
        s.append(f[i])
m = min(s)
p = []
for i in range(len(f) - 1):
    if f1(f[i], f[i + 1]) and f2(f[i], f[i + 1], m):
        p.append(f[i] ** 2 + f[i + 1] ** 2)
print(len(p), max(p))
