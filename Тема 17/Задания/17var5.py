a = list(map(int, open('17var5.txt').readlines()))
def f(x, y):
    if x % 10 == 5 and y % 10 == 5:
        return True
    return False
m = []
for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        m.append(a[i] - a[i + 1])
print(len(m), min(m) if abs(min(m)) > max(m) else max(m))