# Номер студента, оценки за 4 предмета, средний балл, кол-во двоек
marks = []

with open('26.3.txt') as f:
    n = int(f.readline())
    for line in f:
        line = list(map(int, line.split()))
        marks.append(line + [sum(line[1:]) / 4] + [sum(1 if x == 2 else 0 for x in line[1:5])])

marks.sort(key=lambda x: (x[6], -x[5], x[0]))
print(marks[int(n * 0.25) - 1])

for item in marks:
    if item[6] > 2:
        print(item)
        break