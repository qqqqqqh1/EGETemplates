from itertools import *
words = list(product('АНП', repeat=5))
print(*(words[200]))