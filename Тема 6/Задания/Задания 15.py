'''
from turtle import *
tracer(0)
k = 40
screensize(4000, 4000)

for i in range(4):
    forward(14 * k)
    right(90)

for i in range(5):
    forward(5 * k)
    right(45)

up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
'''
print(59)