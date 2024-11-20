p = range(10, 15)
q = range(10, 20)
r = range(5, 15)
min_len = 100
for begin in range(100):
    for end in range(100):
        a = range(begin, end)
        if all(((x in a) <= (x in p)) == ((x in q) <= (x in r)) for x in range(100)):
            min_len = min(min_len, end - begin)
print(min_len)