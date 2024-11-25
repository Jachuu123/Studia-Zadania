def pot(a, b):
    rez = 1
    while b>0:
        if b%2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez

def pot(a, b):
    if not b:
        return 1
    if b%2:
        return a*pot(a*a,b//2)
    return pot(a*a,b/2)

#za każdym razem kiedy b%2 == 1 czyli inaczej
#kiedy w zapisie binarnym potęgi występuje 1, wykonywana jest dodatkowa operacja mnożenia w obu algorytmach
#zatem aby uzyskać jak najmniejszą liczbę potęg należy zminimalizować liczbe 1 i ilość liczb zapisu binarnego.
#najmniej mnożeń wystąpi dla liczby 2 ^ k (najmniej liczb i najwięcej 0)
#najwięcej mnożeń wystąpi dla liczby (2 ^ (k+1)) - 1 (najwięcej liczb i najwięcej 1)
