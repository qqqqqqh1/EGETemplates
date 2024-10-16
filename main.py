ip = '120.91.176.213'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
ip = '120.91.174.205'
print()
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))

'''
Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0.
Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 5?
В ответе укажите только число
'''
count = 0
for i in range(256 - 248):
    for j in range(256):
        # Начальный адрес сети
        ip = f'172.16.{168 + i}.{j}'
        s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
        if s.count('1') % 5 != 0:
            count += 1
print(count)
