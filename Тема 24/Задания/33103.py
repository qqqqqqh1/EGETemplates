l = open('33103.txt').readlines()
cnt = 0
for f in l:
    if f.count('A') > f.count('E'):
        cnt += 1
print(cnt)