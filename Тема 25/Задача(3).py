'''Пусть M — сумма минимального и максимального натуральных делителей целого числа, не считая единицы и
самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю. Напишите программу,
которая перебирает целые числа, большие 800000, в порядке возрастания и ищет среди них такие, для которых
значение M оканчивается на 8. Вывести первые 5 найденных чисел и соответствующие им значения M.
Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число,
затем — значение М. Строки выводятся в порядке возрастания найденных чисел.'''
def f(x):
    a = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            a.append(i)
    if len(a) > 1:
        return min(a) + max(a)
    return False

for i in range(800000, 100000000):
    if f(i):
        if f(i) % 10 == 8:
            print(i, f(i))