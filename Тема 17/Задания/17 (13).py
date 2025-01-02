a = list(map(int, open('17 (13).txt').readlines()))
def f(x, y):
    if x % 3 == 0 or y % 3 == 0:
        if (x + y) % 5 == 0:
            return True
m = []
for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        m.append(a[i] + a[i + 1])
print(len(m), max(m))
