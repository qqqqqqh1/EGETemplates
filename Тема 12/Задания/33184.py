def convert(s):
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    return s


m = 1000
min_len = 0
for l in range(101, 1000):
    cnt = convert('1' * l).count('1')
    if cnt < m:
        m = cnt
        min_len = l
print(min_len)