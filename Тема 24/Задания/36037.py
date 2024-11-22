line = 'XZZYXYXYXXXXXXYXYXZZYZZZZZXZZYX'
parts = list(map(len, line.split('XZZY')))
parts[0] -= 3
parts[-1] -= 3
print(parts)
print(max(parts) + 6)
