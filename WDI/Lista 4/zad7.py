from wdi import *

n = int(input("Podaj n:"))
k = 0
liczby = Array(10)

while n > 0:
    if liczby[n%10] == 0:
        k += 1
    liczby[n%10]+=1
    n //= 10

print(k)