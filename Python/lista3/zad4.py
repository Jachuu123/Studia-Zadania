import turtle
from tkinter import *

skk = turtle.Turtle()
kat = 0
skk.right(180)
while kat != 360:

    skk.right(-60)
    skk.forward(50)
    skk.left(-120)
    skk.forward(50)
    skk.left(-30)

    for i in range(4):
        skk.forward(50)
        skk.right(90)

    skk.left(90)

    skk.right(-36)
    kat = kat + 36



turtle.done() 