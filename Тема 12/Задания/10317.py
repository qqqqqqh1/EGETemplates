def convert(s :str):
    while '333' in s or '888' in s:
        if '333' in s:
            s = s.replace('333', '8', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    return s

print(convert(str(125 * '8')))