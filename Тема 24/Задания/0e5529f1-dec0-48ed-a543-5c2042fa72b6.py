f = open('0e5529f1-dec0-48ed-a543-5c2042fa72b6.txt').readline()
f = (f.
     replace('--', ' ').
     replace('**', ' ').
     replace('*-', ' ').
     replace('-*', ' ').
     replace('-0', ' ').
     replace('*0', ' ').
     split())
print(len(max(f, key=len)))
print(max(f, key=len))