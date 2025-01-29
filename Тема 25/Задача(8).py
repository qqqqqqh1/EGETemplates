'''Напишите программу, которая ищет среди целых чисел больших 900000 первые четыре числа,
имеющие делитель, который оканчивается на 3, но не равен 3. Для каждого найденного числа запишите
это число и минимальный такой делитель.'''
def f(x):
    a = []
    for i in range(13, 1000000, 10):
        if x % i == 0:
            a.append(i)
        if len(a) == 1:
            break
    return a
for i in range(900000, 100000000):
    if f(i):
        print(i, f(i))