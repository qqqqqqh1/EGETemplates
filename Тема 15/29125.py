for a in range(128):
    if all((4 * x + 3 * y < a) or (x > y) or (y > 13) for x in range(128) for y in range(128)):
        print(a)
        break