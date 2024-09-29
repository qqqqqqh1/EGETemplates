for num in range(2, 1000000):
    b = bin(num)[2:]
    b = b.replace('0', '3')
    b = b.replace('1', '0')
    b = b.replace('3', '1')
    b.lstrip('0')
    b = int(b, 2)
    if num - b == 999:
        print(num)
        break
