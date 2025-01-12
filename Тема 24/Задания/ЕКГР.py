f = open('24ЕКГР.txt').readline()
l = k = kmax = 0
for right in range(4, len(f) - 1):
    k += f[right - 4:right] == 'FSRQ'
    while k > 80:
        k -= f[l:l + 4] == 'FSRQ'
        l += 1
    if k == 80:
        kmax = max(right - l, kmax)
print(kmax)