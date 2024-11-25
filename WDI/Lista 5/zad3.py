def gcd(n, m):
    if m == 0:
        return n
    if n == 0:
        return m

    if n < m:
        return gcd(m, n)

    # Znajdź największą liczbę nieparzystą dzielącą oba n i m
    oddcnt = 0
    while n % 2 == 0 and m % 2 == 0:
        n //= 2
        m //= 2
        oddcnt += 1

    # Główna pętla algorytmu
    while n != m:
        if n % 2 == 0:
            n //= 2
        elif m % 2 == 0:
            m //= 2
        elif n > m:
            n = (n - m) // 2
        else:
            m = (m - n) // 2

    # Największy wspólny dzielnik to `n * 2^oddcnt`
    return n * (2 ** oddcnt)

# Przykład użycia
n = 48
m = 18
print(f"NWD({n}, {m}) = {gcd(n, m)}")
