def convert(s):
    while '00' not in s:
        if '011' in s:
            s = s.replace('011', '101', 1)
        else:
            s = s.replace('01', '40', 1)
            s = s.replace('02', '20', 1)
            s = s.replace('0222', '1401', 1)
    return s

for i in range(1000):
    c = '0' + '1' * i + '2' * i + '0'
    d = convert(c)
    if d.count('1') == 8 and d.count('2') == 13:
        print(d.count('4'))