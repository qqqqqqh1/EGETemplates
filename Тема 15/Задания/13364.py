p = range(130, 171)
q = range(150, 185)
min_len = 100
for begin in range(100):
    for end in range(begin, 100):
        a = range(begin, end)
        if all((x in p) <= (((x in q) and (x not in a)) <= (x not in p)) for x in range(-100, 100)):
            min_len = min(min_len, end - begin)
print(min_len)