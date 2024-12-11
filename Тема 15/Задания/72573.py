p = range(3, 43)
q = range(18, 91)
r = range(72, 115)
min_len = 10000
for begin in range(100):
    for end in range(begin, 100):
        a = range(begin, end)
        if all((x in q) <= ((not(x in p)) <= (((not(x in r)) and (not (x in a))) <= (not (x in q)))) for x in range(100)):
            min_len = min(min_len, end - begin)
print(min_len)