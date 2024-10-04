def convert(s :str):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        elif '>2' in s:
            s = s.replace('>2', '2>', 1)
        elif '>0' in s:
            s = s.replace('>0','1>', 1)
    return s

def is_simple(n):
    for i in range(2, 1 + n // 2):
        if n % i == 0:
            return False
    return True



for n1 in range(1000):
    s = convert('>' + '0' * 39 + '1' * n1 + '2' * 39)
    total_sum = s.count('1') + s.count('2') * 2
    if is_simple(total_sum):
        print(n1)
        break