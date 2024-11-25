def usun_duplikaty(L):
    # Sortowanie listy L
    L.sort()

    # Lista wynikowa
    wynik = []

    # Iteracja po posortowanej liście
    for element in L:
        # Dodajemy element do wyniku tylko, jeśli jest różny od ostatniego dodanego
        if not wynik or wynik[-1] != element:
            wynik.append(element)

    return wynik


# Test
print(usun_duplikaty([1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]))
