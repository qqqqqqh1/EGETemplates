p = range(17, 40)
q = range(20, 57)
min_len = 100
for begin in range(100):
    for end in range(begin, 100):
        a = range(begin, end)
        if all((not(x in a)) <= (((x in p) and (x in q)) <= (x in a)) for x in range(100)):
            min_len = min(min_len, end - begin)
print(min_len)