import math


def find_k_hard(n, m):
    if m <= 1:
        return 0  # Jeśli m <= 1, to k = 0, bo n^0 = 1
    left, right = 0, m  # Początkowy zakres wyszukiwania

    while left < right:
        mid = (left + right) // 2
        if n ** mid >= m:
            right = mid  # Szukamy mniejszego k
        else:
            left = mid + 1  # Szukamy większego k

    return left


# Przykład użycia:
n = 3
m = 100
print(f"Najmniejsza liczba k, taka że {n}^k >= {m}: {find_k_hard(n, m)}")
