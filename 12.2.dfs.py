def czy_bezpieczne(stan):
    """Sprawdza, czy dany stan jest bezpieczny (bez konsumpcji)."""
    lewy_brzeg, prawy_brzeg = stan
    # Jeśli koza i wilk są razem bez przewoźnika
    if 'K' in lewy_brzeg and 'W' in lewy_brzeg and 'P' not in lewy_brzeg:
        return False
    if 'K' in prawy_brzeg and 'W' in prawy_brzeg and 'P' not in prawy_brzeg:
        return False
    # Jeśli koza i kapusta są razem bez przewoźnika
    if 'K' in lewy_brzeg and 'C' in lewy_brzeg and 'P' not in lewy_brzeg:
        return False
    if 'K' in prawy_brzeg and 'C' in prawy_brzeg and 'P' not in prawy_brzeg:
        return False
    return True

def dfs(stan, historia):
    """Przeszukiwanie w głąb, aby znaleźć rozwiązanie."""
    if stan == (set(), {'W', 'K', 'C', 'P'}):  # Jeśli wszystko jest na prawym brzegu
        return historia

    lewy_brzeg, prawy_brzeg = stan
    przewoźnik = 'P' in lewy_brzeg  # Sprawdź, gdzie jest przewoźnik
    aktualny_brzeg = lewy_brzeg if przewoźnik else prawy_brzeg
    drugi_brzeg = prawy_brzeg if przewoźnik else lewy_brzeg

    for pasazer in aktualny_brzeg:
        if pasazer == 'P':
            continue  # Przewoźnik zawsze musi płynąć
        # Wykonaj ruch
        nowy_lewy = lewy_brzeg.copy()
        nowy_prawy = prawy_brzeg.copy()

        if przewoźnik:
            nowy_lewy.remove('P')
            nowy_prawy.add('P')
            nowy_lewy.remove(pasazer)
            nowy_prawy.add(pasazer)
        else:
            nowy_prawy.remove('P')
            nowy_lewy.add('P')
            nowy_prawy.remove(pasazer)
            nowy_lewy.add(pasazer)

        nowy_stan = (nowy_lewy, nowy_prawy)
        if czy_bezpieczne(nowy_stan) and nowy_stan not in historia:
            wynik = dfs(nowy_stan, historia + [nowy_stan])
            if wynik:
                return wynik
    return None

# Stan początkowy
stan_poczatkowy = ({'W', 'K', 'C', 'P'}, set())
historia = dfs(stan_poczatkowy, [stan_poczatkowy])
for i, stan in enumerate(historia):
    print(f"Krok {i}: Lewy brzeg: {stan[0]}, Prawy brzeg: {stan[1]}")
