def oblicz_G(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    G0, G1, G2 = 1, 1, 1

    for i in range(3, n + 1):
        Gn = G0 + G1 + G2
        G0, G1, G2 = G1, G2, Gn

    return G2

n = 10
print(oblicz_G(n))  # Wynik to G10