from turtle import Turtle, tracer
from random import choice

rows = [row.strip() for row in open("pixels.txt").readlines()]

t = Turtle()
t.speed(0)
t.penup()
# tracer(0,1)
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

pixels_with_coord = []

for row in rows:
    for pixel in row.split():
        temp = pixel.strip('(').strip(')')
        a = temp.split(",")
        field = tuple([int(x)/255 for x in a])
        predicate = [x,y,field]
        pixels_with_coord.append(predicate)
        x+=1

    x = 0
    y+=1

temp = []
while len(pixels_with_coord):
        pxl = choice(pixels_with_coord)
        draw_pixel(pxl[0]*5, pxl[1]*5, pxl[2])
        pixels_with_coord.remove(pxl)

input()