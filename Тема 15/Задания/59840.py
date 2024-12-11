for a in range(100):
    if all(48 != (y + 2 * x) or (a < x) or (a < y) for x in range(100) for y in range(100)):
        print(a)