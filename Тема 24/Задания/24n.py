f = open('24n.txt').readline()
f = f.replace('DE', 'D E').split()
m = 0
for i in range(len(f) - 240):
    d = ''.join(f[i:i + 241])
    if len(d) > m:
        m = len(d)
print(m)