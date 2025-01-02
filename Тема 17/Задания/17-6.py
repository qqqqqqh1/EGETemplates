f = list(map(int, open('17-6.txt').readlines()))
m = []
def h(x, y, z):
    if bin(x)[2:].count('1') == 2 and bin(y)[2:].count('1') == 2 and bin(z)[2:].count('1') == 2:
        return True
for i in range(len(f) - 2):
    if h(f[i], f[i + 1], f[i + 2]):
        m.append(f[i] + f[i + 1] + f[i + 2])
print(len(m), max(m))
