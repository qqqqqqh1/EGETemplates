f = open('27696.txt').readline()
f = f.replace('D', ' ').replace('R', ' ').split()
print(len(max(f, key=len)))