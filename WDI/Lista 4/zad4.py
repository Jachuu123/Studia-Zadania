from wdi import *

def nwd(a, b): #algorytm euklidesa
    while b != 0:
        a, b = b, a % b
    return a

liczby = Array(10)

n = int(input("Podaj n:"))
k = int(input("Podaj k:"))

a = Array(k)
for i in range(k-1):
    a[i] = input()

