for a in range(100):
    if all(((x & 25) != 0) <= (((x & 17) == 0) <= ((x & a) != 0)) for x in range(100)):
        print(a)