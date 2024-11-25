def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def energia(n):
    steps = 0
    while n != 1:
        n = F(n)
        steps += 1
    return steps


def analiza_collatza(a, b):
    energie = [energia(i) for i in range(a, b + 1)]

    srednia = sum(energie) / len(energie)
    mediana = sorted(energie)[len(energie) // 2] if len(energie) % 2 != 0 else \
        (sorted(energie)[len(energie) // 2 - 1] + sorted(energie)[len(energie) // 2]) / 2
    maksimum = max(energie)
    minimum = min(energie)

    print("Średnia energia:", srednia)
    print("Mediana energii:", mediana)
    print("Maksymalna energia:", maksimum)
    print("Minimalna energia:", minimum)


# Przykład użycia
analiza_collatza(6, 10)
