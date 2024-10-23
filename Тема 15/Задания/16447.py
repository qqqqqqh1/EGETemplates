for a in range(128):
    if all((2 * x + 3 * y < 30) or (x + y >= a) for x in range(100) for y in range(100)):
        print(a)