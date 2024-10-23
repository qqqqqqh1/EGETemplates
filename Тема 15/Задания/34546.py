p = range(23, 59)
q = range(1, 40)
min_len = 100
for begin in range(100):
    for end in range(100):
        a = range(begin, end)
        if all(((x in p) or (x in a)) <= ((x in q) or x in a) for x in range(100)):
            min_len = min(min_len, end - begin)
print(min_len)            