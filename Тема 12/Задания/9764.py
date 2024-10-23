def f(s):
    while '333' in s or '999' in s:
        if '333' in s:
            s = s.replace('333', '9', 1)
        else:
            s = s.replace('999', '3', 1)
    return s
print(f('9' * 127))