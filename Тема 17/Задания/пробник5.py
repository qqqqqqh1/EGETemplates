a = list(map(int, open('ПРОБНИК_05_задание17.txt').readlines()))
h = []
def f(x):
    if len(str(x)) == 5 and x % 100 == 43:
        return True
m = 0
for i in range(len(a)):
    if f(a[i]):
        m = max(m, a[i])
s = m ** 2
for i in range(len(a) - 2):
    if (f(abs(a[i])) or f(abs(a[i + 1])) or (f(abs(a[i + 2])))) and ((a[i] ** 2 + a[i + 1] ** 2 + a[i + 2] ** 2) <= s):
        h.append(a[i] ** 2 + a[i + 1] ** 2 + a[i + 2] ** 2)
print(len(h), min(h))