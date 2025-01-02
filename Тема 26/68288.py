f = open('68288.txt').readlines()[1:]
d = [0] * 86400
s = 15 * 60 ** 2
e = 21 * 60 ** 2
c = 0
for i in f:
    t1, t2 = map(int, i.split())
    for j in range(t1, t2):
        d[j] += 1
c = max(d[s:e + 1])
k = d[s:e + 1].count(c)
print(c, k)