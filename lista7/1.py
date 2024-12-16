from turtle import Turtle, tracer

rows = [row.strip() for row in open("pixels.txt").readlines()]

t = Turtle()
t.speed(0)
t.penup()
tracer(0,1)

def draw_pixel(x, y, color):
    t.goto(x, y)
    t.begin_fill()
    t.fillcolor(tuple(color))
    for i in range(4):
        t.forward(5)
        t.right(90)
    t.end_fill()

x = 0
y = 0

for row in rows:
    for pixel in row.split():
        temp = pixel.strip('(').strip(')')
        a = temp.split(",")
        field = [int(x)/255 for x in a]
        draw_pixel(x*5, y*5, field)
        x+=1

    x = 0
    y+=1


input()