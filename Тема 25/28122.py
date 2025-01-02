k = []
def f(x):
    m = []
    for i in range(1, x + 1):
        if x % i == 0:
            m.append(i)
    if len(m) == 4:
        return m

for i in range(489_421, 489_441):
    print(f(i))