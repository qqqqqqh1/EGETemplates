a = list(map(int, open('17 (16).txt').readlines()))
o = [h if h % 2 != 0 else 100000 for h in a]
m = min(o)
j = []
def f(x, y, z):
    if ((x % 3 == 0 and y % 3 != 0) or (x % 3 != 0 and y % 3 == 0)) and (abs(x - y) < z):
        return True
for i in range(len(a) - 1):
    if f(a[i], a[i + 1], m):
        j.append(abs(a[i] - a[i + 1]))
print(len(j), max(j))
