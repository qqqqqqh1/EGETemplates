f = list(map(int, open('7619(КЕГЭ).txt').readlines()))
m = []
for i in range(len(f)):
    a = str(f[i])
    if len(a) == 2:
        m.append(a)
mm = max(m)
s = []
for l in range(len(f) - 1):
    if ((len(str(f[l])) == 2 and len(str(f[l + 1])) != 2) or (len(str(f[l + 1])) == 2 and len(str(f[l])) != 2)) and ((int(f[l]) + int(f[l + 1])) % int(mm)) == 0:
        s.append(f[l] + f[l + 1])
print(len(s), max(s))