import turtle
import random
import duze_cyfry
from PYTHON.lista2.duze_cyfry import popraw, daj_cyfre


# Tworzymy funkcję rysującą jeden kwadracik
def rysuj_kwadrat(t, x, y, rozmiar, kolor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(kolor)
    t.begin_fill()
    for _ in range(4):
        t.forward(rozmiar)
        t.left(90)
    t.end_fill()

n = int(421424)
cyfry = []
ilosc_cyfr = len(str(n))

for i in range(0,ilosc_cyfr):
    cyfry.append(n%10)
    n //= 10

cyfry.reverse()
#print(cyfry)

liczba_rysowana = []
tab_pom = []

for i in range(0,ilosc_cyfr):
    print(daj_cyfre())

for r in daj_cyfre(6):
    print (r)


