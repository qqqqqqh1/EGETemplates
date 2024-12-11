f = open('68525.txt').readline()
a = ['Q', 'R', 'W']
d = ['1', '2', '4']
m = 0
c = 1
for i in range(len(f) - 1):
    if (f[i] in a and f[i + 1] in d) or (f[i] in d and f[i + 1] in a):
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)