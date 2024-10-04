def simple(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def convert(s :str):
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    return s

for n1 in range(100, 1000):
    c = '0' + '1' * n1 + '2' * n1 + '0'
    d = convert(c)
    total_sum = int(d.count('1')) + int(d.count('2')) * 2
    if simple(total_sum):
        print(n1)
        break