for a in range(1, 128):
    if all((72 % x == 0) <= (not(120 % x == 0)) or (a - x > 100) for x in range(1, 128)):
        print(a)