import turtle

# Funkcja konwertująca kolor z formatu 0-255 na 0-1
def konwertuj_kolor(rgb):
    return tuple(c / 255 for c in rgb)

# Funkcja do rysowania pojedynczego piksela
def rysuj_piksel(x, y, kolor, bok):
    kolor = konwertuj_kolor(kolor)  # Konwersja koloru na zakres 0-1
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(kolor)
    for _ in range(4):  # Rysowanie kwadratu
        turtle.forward(bok)
        turtle.right(90)
    turtle.end_fill()

# Funkcja do wczytania obrazu z pliku
def wczytaj_obraz(nazwa_pliku):
    obraz = []
    with open(nazwa_pliku, "r") as plik:
        for linia in plik:
            # Wczytanie wiersza obrazu, usunięcie białych znaków i rozdzielenie na piksele
            piksele = linia.strip().split(" ")
            obraz.append([eval(piksel) for piksel in piksele])
    return obraz

# Główna część programu
def rysuj_obraz(obraz, bok_piksela=10):
    turtle.speed(0)  # Maksymalna prędkość rysowania
    turtle.tracer(0, 1)  # Przyspieszenie rysowania
    x_start = -len(obraz[0]) * bok_piksela / 2  # Pozycja początkowa w poziomie
    y_start = len(obraz) * bok_piksela / 2  # Pozycja początkowa w pionie
    for i, wiersz in enumerate(obraz):
        for j, piksel in enumerate(wiersz):
            # Obliczanie pozycji piksela i jego koloru
            x = x_start + j * bok_piksela
            y = y_start - i * bok_piksela
            rysuj_piksel(x, y, piksel, bok_piksela)
    turtle.update()  # Wyświetlenie rysunku

# Wczytanie obrazu z pliku i jego narysowanie
obraz = wczytaj_obraz("pixels.txt")  # Użyj odpowiedniej nazwy pliku
rysuj_obraz(obraz)

turtle.done()
