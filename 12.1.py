from collections import deque

def znajdz_najkrotsza_sciezke(start, koniec, slownik):
    # Sprawdź, czy oba słowa są w słowniku
    if start not in slownik or koniec not in slownik:
        return []

    # Funkcja pomocnicza do sprawdzania, czy dwa słowa różnią się jedną literą
    def roznica_jednej_litery(slowo1, slowo2):
        roznice = sum(1 for a, b in zip(slowo1, slowo2) if a != b)
        return roznice == 1

    # Kolejka BFS
    kolejka = deque([[start]])
    odwiedzone = set([start])

    while kolejka:
        sciezka = kolejka.popleft()
        ostatnie_slowo = sciezka[-1]

        # Jeśli dotarliśmy do końcowego słowa, zwróć ścieżkę
        if ostatnie_slowo == koniec:
            return sciezka

        # Przejdź przez wszystkie możliwe sąsiadujące słowa
        for slowo in slownik:
            if slowo not in odwiedzone and roznica_jednej_litery(ostatnie_slowo, slowo):
                kolejka.append(sciezka + [slowo])
                odwiedzone.add(slowo)

    # Jeśli nie znaleziono ścieżki, zwróć pustą listę
    return []

# Przykładowy słownik czteroliterowych słów (należy podać pełny słownik)
slownik_polskich_slow = {'mąka', 'mika', 'miks', 'kiks', 'keks', 'woda', 'wino', 'woda', 'soda', 'sowa', 'koda'}

# Test dla słów "woda" i "wino"
start = 'woda'
koniec = 'wino'

sciezka = znajdz_najkrotsza_sciezke(start, koniec, slownik_polskich_slow)
print(sciezka)
