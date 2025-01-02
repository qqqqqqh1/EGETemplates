k = open('55643.txt').readlines()
s = [[0] * 10000 for i in range(10000)]
for i in range(int(k[0])):
    row, seat = [int(r) for r in k[1:]]
    s[row][seat] = 1

for i in range(len(s)):
    for j in range(len(s[i])):

