def permutacyjna_postac_normalna(slowo):
    # Tworzymy słownik, który będzie mapował litery na liczby
    mapa_liter = {}
    licznik = 1

    # Lista, która będzie przechowywała numery odpowiadające literom
    wynik = []

    for litera in slowo:
        # Jeśli litera nie była jeszcze odwiedzona, przypisujemy jej nową liczbę
        if litera not in mapa_liter:
            mapa_liter[litera] = licznik
            licznik += 1
        
        # Dodajemy odpowiedni numer do wyniku
        wynik.append(str(mapa_liter[litera]))

    # Łączymy liczby w jedną wartość z separatorem "-"
    return "-".join(wynik)

# Przykłady użycia
print(permutacyjna_postac_normalna("tak"))      # 1-2-3
print(permutacyjna_postac_normalna("nie"))      # 1-2-3
print(permutacyjna_postac_normalna("tata"))     # 1-2-1-2
print(permutacyjna_postac_normalna("indianin")) # 1-2-3-1-4-2-1-2
