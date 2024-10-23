b = range(70, 91)
for a in range(1, 128):
    if all((x % a == 0) or ((x in b) <= (not(x % 27 == 0))) for x in range(1, 128)):
        print(a)
