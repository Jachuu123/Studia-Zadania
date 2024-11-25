def silina (n):
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

#print(str(12))
for i in range(4,34):
    dl =len(str(silina(i)))
    pom = "cyfr"
    rem = [2,3,4]
    if((dl%10 in rem) and not (dl > 10 and dl < 22)):
        pom = "cyfry"

    print(f"{i}! ma {len(str(silina(i)))} {pom}")
    #