'''
ip = '115.127.30.120'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
'''
ip = '98.162.71.94'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
ip = '98.162.71.64'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
'''
01100010 10100010 01000111 01011110
01100010 10100010 01000111 01000000
'''
print(int('11101', 2))