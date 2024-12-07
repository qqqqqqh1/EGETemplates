f = open("59702.txt").readline()
f = f.split('Y')
m = 0
for i in range(len(f)):
    d = 'Y'.join(f[i:i + 151])
    if len(d) > m:
        m = len(d)
print(m)