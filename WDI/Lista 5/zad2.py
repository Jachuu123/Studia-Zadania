from WDI.wdi import *

def silniowa_reprezentacja(n):
    max_silnia = 12
    max_silnia += 1
    wartosci_silni = Array(max_silnia)
    wystapienia_silni = Array(max_silnia)

    for i in range(max_silnia):
        wartosci_silni[i] = 1

    for i in range(1,max_silnia):
        wartosci_silni[i] = wartosci_silni[i-1] * i
        if wartosci_silni[i] > n:
            ilosc_silni = i
            break
    else:
        ilosc_silni = max_silnia

    for i in range(ilosc_silni -1, 0, -1): # czytanie tablicy od tyłu od ilosc_silni do 0
        wystapienia_silni[i] = n // wartosci_silni[i] # za każdym razem zmniejszamy n
                                            # o co najmniej największą silnie która się w niej mieści
        n %= wartosci_silni[i]

        print(wystapienia_silni[i],end=" ")

silniowa_reprezentacja(1000)
