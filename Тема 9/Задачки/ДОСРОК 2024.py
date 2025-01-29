f = open('ДОСРОК 2024.txt')
k = 0
for i in f:
    a = [int(x) for x in i.split()]
    if max(a) < (sum(a) - max(a)):
        if (a[0] + a[1] == a[2] + a[3]) or (a[0] + a[2] == a[1] + a[3]) or (a[0] + a[3] == a[1] + a[2]):
            k += 1
print(k)
