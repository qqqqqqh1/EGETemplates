for a in range(100):
    if all((x < a) or (y < a) or (y > (x - 5)) or (y <(2 * x - 15)) for x in range(100) for y in range(100)):
        print(a)
        break