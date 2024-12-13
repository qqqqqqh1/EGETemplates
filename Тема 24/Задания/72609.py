line = open('72609.txt').readline()
"""
1) B###
2) Не может быть: B-, *-, --, **, B0
3) 
Ответ: 68
"""
line = (line
        .replace('B-', 'B -')
        .replace('-B', '- B')
        .replace('*B', '* B')
        .replace('BB', 'B B')
        .replace('*-', '* -')
        .replace('-*', '- *')
        .replace('--', '- -')
        .replace('**', '* *')
        .replace('B0', 'B 0')
        .replace('0B', '0 B')
        .replace('1B', '1 B')
        .replace('2B', '2 B')
        .replace('3B', '3 B')
        .replace('4B', '4 B')
        .replace('5B', '5 B')
        .replace('6B', '6 B')
        .replace('B*', 'B *')
        .replace('A', ' ')
        .replace('C', ' ')
        .replace('D', ' ')
        )
list = []
for p in line.split():
    if p[0] == 'B':
        list.append(p.strip('*').strip('-'))
print(max(list, key=len))
print(len(max(list, key=len)))


