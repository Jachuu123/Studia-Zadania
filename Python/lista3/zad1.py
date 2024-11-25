def sito(n):
    tab = []
    for i in range(n+1):
       tab.append(0)
    tab[0] = tab[1] = 1
    i = 2
    while i*i <= n:
        if tab[i] == 0:
            for j in range(i*i, n+1, i):
                tab[j] = 1
        i += 1 

    return tab

def szczęśliwa(n):
    liczba = str(n)
    for i in range(len(liczba)-2):
        if liczba[i] == '7':
            if liczba[i+1] == '7' and liczba[i+2] == '7':
                return True
    return False


n = int(input("Podaj wielkość sita: "))

tab = sito(n)
licznik = 0

for i in range(n + 1):
    if tab[i] == 0 and szczęśliwa(i):
        licznik += 1
print(licznik)


