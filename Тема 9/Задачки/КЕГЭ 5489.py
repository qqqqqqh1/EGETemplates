f = open('КЕГЭ 5489.txt')
k = 0
for i in f:
    a = [int(x) for x in i.split()]
    pov = [a.count(x) for x in a]
    ch = [x for x in a if x % 2 == 0]
    nech = [x for x in a if x % 2 != 0]
    if pov.count(1) == 5:
        if len(ch) > len(nech):
            if sum(ch) < sum(nech):
                k += 1
print(k)