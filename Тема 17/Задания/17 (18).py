f = list(map(int, open('17 (18).txt').readlines()))
s = []
for i in f:
    if i % 2 != 0:
        s.append(i)
sr = sum(s) / len(s)
def d(x, y, z, w):
    a = x % 3
    c = y % 3
    g = z % 3
    if a != c and c != g and a != g:
        if (x < w and y >= w and z >= w) or (x >= w and y < w and z >= w) or (x >= w and y >= w and z < w):
            return True


m = []
for i in range(len(f) - 2):
    if d(f[i], f[i + 1], f[i + 2], sr):
        m.append(f[i] + f[i + 1] + f[i + 2])
print(len(m), max(m))
