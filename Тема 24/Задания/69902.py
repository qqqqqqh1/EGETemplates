f = open('69902.txt').readline()
f = f.split('DE')
m = 0
for i in range(len(f)):
    d = "DE".join(f[i:i + 241])
    if len(d) > m:
        m = len(d)
print(m)