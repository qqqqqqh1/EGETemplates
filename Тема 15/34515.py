for a in range(128):
    if all((x & 41 != 0) <= ((x & 33 == 0) <= (x & a != 0)) for x in range(100)):
        print(a)