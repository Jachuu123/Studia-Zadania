import turtle
import math


def drzewo_pitagorasa(t, dlugosc, poziom, nachylenie_galezi):
    if poziom == 0:
        return
    t.forward(dlugosc)
    pozycja = t.position()
    kat = t.heading()

    # Lewa
    t.left(nachylenie_galezi)
    drzewo_pitagorasa(t, dlugosc * math.sqrt(2) / 2, poziom - 1, nachylenie_galezi)

    t.penup()
    t.setposition(pozycja)
    t.setheading(kat)
    t.pendown()

    # Prawa
    t.right(nachylenie_galezi)
    drzewo_pitagorasa(t, dlugosc * math.sqrt(2) / 2, poziom - 1, nachylenie_galezi)

    t.penup()
    t.setposition(pozycja)
    t.setheading(kat)
    t.pendown()

    t.backward(dlugosc)


turtle.speed(0)
turtle.delay(0)
turtle.bgcolor("white")
t = turtle.Turtle()
t.left(90)
t.color("green")

dlugosc_pnia = 100
poziom_rekurencji = 15
nachylenie_galezi = 30

t.penup()
t.goto(0, -300)
t.pendown()
drzewo_pitagorasa(t, dlugosc_pnia, poziom_rekurencji,nachylenie_galezi)

turtle.done()
