from lista2.duze_cyfry import daj_cyfre

n = 12354
n = str(n)


for i in range(len(str(n))):
    for r in daj_cyfre(int(n[i])):
        print(r)
    print()