count = 0
for i in range(256-248):
    ip = f'122.159.136.{144+i}'
    s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
    if s.count('1') % 4 != 0:
        count += 1
print(count)