from duze_cyfry import daj_cyfre

n = 12354
n = str(n)

wynik = []

for j in range(6):
    for i in n:
        for r in daj_cyfre(int(i)):
            wynik.append(r)

#print(wynik)

for i in range(5):
    for j in range(int(n)):
        print(wynik[j][i],end="")