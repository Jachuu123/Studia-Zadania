from wdi import *

def podobne(n,m):

    liczby = Array(10,2)

    while n > 0:
        liczby[n%10][0]+=1
        n //= 10

    while m > 0:
        liczby[m%10][1]+=1
        m //= 10

    for i in range(9):
        if liczby[i][0] != liczby[i][1]:
            return False
    return True

n = int(input("Podaj n:"))
m = int(input("Podaj m:"))

print(podobne(n,m))