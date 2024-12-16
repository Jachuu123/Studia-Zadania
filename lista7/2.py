import turtle
import random

def konwertuj_kolor(rgb):
    return tuple(c / 255 for c in rgb)

def rysuj_piksel(x, y, kolor, bok):
    kolor = konwertuj_kolor(kolor)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(kolor)
    for _ in range(4):
        turtle.forward(bok)
        turtle.right(90)
    turtle.end_fill()

def wczytaj_obraz(nazwa_pliku):
    obraz = []
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            piksele = linia.strip().split(" ")
            obraz.append([eval(piksel) for piksel in piksele])
    return obraz

def rysuj_obraz_losowo(obraz, bok_piksela=10):
    turtle.speed("fastest")
    x_start = -len(obraz[0]) * bok_piksela / 2
    y_start = len(obraz) * bok_piksela / 2

    piksele = []
    for i, wiersz in enumerate(obraz):
        for j, piksel in enumerate(wiersz):
            x = x_start + j * bok_piksela
            y = y_start - i * bok_piksela
            piksele.append((x, y, piksel))

    random.shuffle(piksele)

    for x, y, kolor in piksele:
        rysuj_piksel(x, y, kolor, bok_piksela)

obraz = wczytaj_obraz("pixels.txt")
rysuj_obraz_losowo(obraz)

turtle.done()
