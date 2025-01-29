f = open('24_2024_ОСН_День1.txt').readline().replace('CD', 'C D').split()
d = 0
j = 0
for i in range(len(f)):
    m = len(''.join(f[i: i + 141]))
    j = max(m, j)
print(j)