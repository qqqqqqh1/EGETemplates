string = open('59849.txt').readline()
alpha = '0123456789ABCDEFGHIJKLMNOP'
lst = []
cnt = 0
for i in range(len(string)):
    if string[i] in alpha:
        cnt += 1
        lst.append(cnt)
    else:
        cnt = 0
print(max(lst))
