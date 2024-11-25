def pow(a, b):
    w = 1
    while b > 0:
        if b%2 == 0:
            w*=a;
        a*=a
        b//=2
    return w

n = int(input("Podaj n:"))
x = int(input("Podaj x:"))
print("zad 1.a")

if n % 2 == 0:
    print(n)
else:
    print(-n)

# O(1)

print("zad 1.b")

suma = 0
for i in range(1,n):
    if i % 2 == 0:
        suma += 1/i
    else:
        suma += (-1)/i
print(suma)

#O(n)

print("zad 1.c")
suma = 0
for i in range(1,n):
    suma += i * pow(x,i)

# O(n*log n)