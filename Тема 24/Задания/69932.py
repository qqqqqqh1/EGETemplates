from itertools import product

line = open('69932.txt').readline()
for p in product('*-0', repeat=2):
    line = line.replace(p[0] + p[1], f'{p[0]} {p[1]}')
parts = line.split()
for i in range(len(parts)):
    parts[i] = parts[i].strip('*').strip('-').lstrip('0')
print(len(max(parts, key=len)))
print(max(parts, key=len))