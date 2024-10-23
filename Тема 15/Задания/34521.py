for a in range(500):
    if all((x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0)) for x in range(500)):
        print(a)