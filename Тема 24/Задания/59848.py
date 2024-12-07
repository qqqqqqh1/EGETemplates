f = open('59848.txt').readline()
apl = 'OPQRSTUVWXYZ'
m = []
for i in apl:
    f = f.replace(i, ' ')
f = f.split()
for j in f:
    if j[0] != '0':
        m.append(len(j))
print(max(m))