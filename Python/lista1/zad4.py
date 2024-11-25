from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    haslo = ""
    while len(haslo) < n:
        haslo+=losuj_fragment()
        if(len(haslo) > n):
            haslo = ""
    print(haslo)

for i in range(10):
    losuj_haslo(8)

print()

for i in range(10):
    losuj_haslo(12)
