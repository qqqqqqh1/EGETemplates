f = list(map(int, open('17-1.txt').readlines()))
def g(x, y, z):
    if x < y < z:
            return True
m = []
j = []
for i in range(len(f) - 2):
    if g(f[i], f[i + 1], f[i + 2]):
        j.append(f[i + 2] - f[i])
        m.append(f[i] + f[i + 2] + f[i + 1])
print(len(m), min(j))
