def convert(s):
    while ('25' in s) or ('355' in s) or ('555' in s):
        s = s.replace('25', '5', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    return s

'''
def convert(s):
    while ('25' in s) or ('355' in s) or ('555' in s):
        if '25' in s:
            s = s.replace('25', '5', 1)
        elif '355' in s:
            s = s.replace('355', '52', 1)
        elif '555' in s:
            s = s.replace('555', '3', 1)
    return s
'''

for n in range(4, 100):
    a = '2' + '5' * n
    b = convert(a)
    if b.count('2') * 2 + b.count('3') * 3 + b.count('5') * 5 == 17:
        print(n)
        break