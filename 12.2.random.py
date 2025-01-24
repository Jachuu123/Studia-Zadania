import random

def losowe(stan):
    """Wykonuje losowe ruchy, aż znajdzie rozwiązanie."""
    historia = [stan]
    while stan != (set(), {'W', 'K', 'C', 'P'}):  # Dopóki nie osiągniemy celu
        lewy_brzeg, prawy_brzeg = stan
        przewoźnik = 'P' in lewy_brzeg
        aktualny_brzeg = lewy_brzeg if przewoźnik else prawy_brzeg
        drugi_brzeg = prawy_brzeg if przewoźnik else lewy_brzeg

        # Wybierz losowo, kogo zabrać
        pasazer = random.choice(list(aktualny_brzeg))

        nowy_lewy = lewy_brzeg.copy()
        nowy_prawy = prawy_brzeg.copy()

        if przewoźnik:
            nowy_lewy.remove('P')
            nowy_prawy.add('P')
            if pasazer != 'P':
                nowy_lewy.remove(pasazer)
                nowy_prawy.add(pasazer)
        else:
            nowy_prawy.remove('P')
            nowy_lewy.add('P')
            if pasazer != 'P':
                nowy_prawy.remove(pasazer)
                nowy_lewy.add(pasazer)

        nowy_stan = (nowy_lewy, nowy_prawy)
        if czy_bezpieczne(nowy_stan):
            stan = nowy_stan
            historia.append(stan)
    return historia

# Stan początkowy
stan_poczatkowy = ({'W', 'K', 'C', 'P'}, set())
historia = losowe(stan_poczatkowy)
for i, stan in enumerate(historia):
    print(f"Krok {i}: Lewy brzeg: {stan[0]}, Prawy brzeg: {stan[1]}")
