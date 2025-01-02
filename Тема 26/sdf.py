f = open('sdf.txt').readlines()[1:]
r = int(open('sdf.txt').readline())
summ = 0
rich = []
for s in f:
    a1, a2, a3 = map(int, s.split())
    summ += a2
sred = summ / r
for s in f:
    a1, a2, a3 = map(int, s.split())
    if a2 > sred and a3 == 0:
        rich.append([a1, a2])
a = 0
c = 0
for i in range(len(rich) - 1):
    c += 1
    if rich[i][1] > rich[i + 1][1]:
        a = rich[i][1]
    else:
        a = rich[i + 1][1]
s = rich[c][0]
print(s, a)