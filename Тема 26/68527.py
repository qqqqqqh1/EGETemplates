f = list(map(int, open('68527.txt').readlines()[1:]))
f.sort(reverse=True)
c = 1
l = 0
k = f[0]
for i in range(1, len(f)):
    if k - f[i] > 3:
        c += 1
        k = f[i]
print(c, k)



