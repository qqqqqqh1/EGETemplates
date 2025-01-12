from turtle import *
tracer(0)
k = 30
screensize(2000, 2000)
left(90)
for i in range(4):
    forward(16 * k)
    right(90)
    forward(22 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(4):
    forward(57 * k)
    right(90)
    forward(75 * k)
    right(90)
up()
for x in range(-k, k):
    for y in range(-k, k):
        dot(3)
        goto(x * k, y * k)
exitonclick()
update()
