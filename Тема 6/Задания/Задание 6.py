'''
from turtle import *

tracer(0)
k = 30
screensize(2000, 2000)
for i in range(2):
    forward(3 * k)
    left(90)
    backward(10 * k)
    left(90)
up()
backward(10 * k)
right(90)
forward(8 * k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)

up()
for x in range(-k, k):
    for y in range(-k, k):
        dot(3)
        goto(x * k, y * k)
exitonclick()
'''
print(185)