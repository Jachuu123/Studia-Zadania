import turtle
import random

# Ustawienia dla żółwia
t = turtle.Turtle()
t.speed(0)  # Maksymalna prędkość rysowania
t.hideturtle()
turtle.bgcolor("white")

# Parametry siatki
grid_size = 20  # Liczba kwadratów w jednym wierszu i kolumnie
square_size = 20  # Rozmiar pojedynczego kwadratu
block_size = 5  # Rozmiar bloku (np. 3x3 kwadraty)


# Funkcja do rysowania kwadratu w danej pozycji z podanym kolorem
def draw_square(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    t.end_fill()


# Funkcja generująca losowy jasny kolor
def random_light_color():
    return (random.uniform(0.7, 1.0), random.uniform(0.7, 1.0), random.uniform(0.7, 1.0))


# Funkcja generująca losowy ciemny kolor
def random_dark_color():
    return (random.uniform(0.3, 0.6), random.uniform(0.3, 0.6), random.uniform(0.3, 0.6))


# Rysowanie siatki z większymi jasnymi i ciemnymi blokami, ale z losowymi kolorami w każdym kwadracie
start_x = -grid_size * square_size // 2
start_y = grid_size * square_size // 2

for row in range(0, grid_size, block_size):
    for col in range(0, grid_size, block_size):
        # Sprawdzenie czy blok powinien być jasny czy ciemny
        is_light_block = (row // block_size + col // block_size) % 2 == 0

        # Rysowanie każdego kwadratu w bloku
        for i in range(block_size):
            for j in range(block_size):
                # Sprawdź, czy nie wychodzimy poza siatkę
                if row + i < grid_size and col + j < grid_size:
                    x = start_x + (col + j) * square_size
                    y = start_y - (row + i) * square_size

                    # Wybierz losowy jasny lub ciemny kolor w zależności od rodzaju bloku
                    color = random_light_color() if is_light_block else random_dark_color()
                    draw_square(x, y, color)

# Zakończenie programu
turtle.done()
