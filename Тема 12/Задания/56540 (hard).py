from itertools import permutations


def convert(s):
    while '00' not in s:
        if '011' in s:
            s = s.replace('011', '101', 1)
        else:
            s = s.replace('01', '40', 1)
            s = s.replace('02', '20', 1)
            s = s.replace('0222', '1401', 1)
    return s

def generate_binary_numbers(n):
    total = 2 * n
    result = []
    for i in range(1 << total):
        if bin(i).count('1') == n:
            result.append(f'{i:0{total}b}')
    return result

for i in range(100):
    for p in generate_binary_numbers(i):
        d = convert('0' + p.replace('0', '2') + '0')
        if d.count('1') == 8 and d.count('2') == 13:
            print(d.count('4'))