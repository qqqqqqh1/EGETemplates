def convert(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s


for n1 in range(100):
    for n2 in range(100):
        for n3 in range(100):
            s = convert('0' + '1' * n1 + '2' * n2 + '3' * n3)
            if s.count('1') == 40 and s.count('2') == 10 and s.count('3') == 8:
                print(n1)
                break
