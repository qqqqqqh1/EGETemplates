f = open('пробник.txt').readline()
f = f.replace('Y', 'Y ').split()
d = 0
s = ''
for i in range(len(f) - 150):
    m = ''.join(f[i: i + 151])
    if len(m) > d:
        d = len(m)
        s = m
print(d - 1)