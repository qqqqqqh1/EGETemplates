'''
from itertools import permutations

table = '13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76'
graph = 'EF EB BE BF BA AB AF AG GA GF GD DG DF DC CD CF FC FD FG FA FB FE'
print('1 2 3 4 5 6 7')
for p in permutations('CDGABEF'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*p)
'''
print('67')