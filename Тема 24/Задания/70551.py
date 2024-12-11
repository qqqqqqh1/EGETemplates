f = open('70551.txt').readline()
f = (f
     .replace('--', ' ')
     .replace('**', ' ')
     .replace('-*', ' ')
     .replace('*-', ' ')



     .strip('0').split())
print((max(f, key=len)))
print(len(max(f, key=len)))