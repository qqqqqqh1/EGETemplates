f = list(map(int, open('db99abbf-4b14-4db7-bc07-f6eb026c08a6.txt').readlines()))
s = []
for i in range(len(f)):
    if f[i] % 32 == 0:
        s.append(f[i])
dl = len(s)
def d(x, y, z):
    if x < 0 or y < 0:
        if (x + y) < z:
            return True
    return False
m = []
for i in range(len(f) - 1):
    if d(f[i], f[i + 1], dl):
        m.append(f[i] + f[i + 1])
print(len(m), max(m))