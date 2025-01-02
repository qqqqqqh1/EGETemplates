a = list(map(int, open('17-6.txt').readlines()))
m = []
def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s
for i in range(len(a) - 2):
    for j in range(i + 1, len(a)):
        for z in range(j + 1, len(a)):
            if f(a[i])[-1] == '2' or f(a[j])[-1] == '2' or f(a[z])[-1] == '2':
                m.append(a[i] + a[j] + a[z])
print(len(m), min(m))