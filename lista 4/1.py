from turtle import *

t = Turtle()
t.teleport(0,250)
t.speed(0)
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(45):
        t.forward(2*3.14*radius / 45)
        t.right(8)
    t.end_fill()

initial_size = 300
for i in range(13, 0, -1):
    color = ''
    if i % 3 == 0:
        color = 'green'
    elif i % 3 == 1:
        color = 'yellow'
    else:
        color = 'aqua'
    draw_circle(initial_size, color)
    initial_size*=0.9
input()
