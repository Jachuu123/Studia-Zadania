
def bezwzgledna(x):
    if x >= 0:
        return x
    else:
        return -x

def nwd(a, b): #algorytm euklidesa
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b): #najmniejszą wspólną wielokrotność
    return bezwzgledna(a * b) // nwd(a, b)

def uproszony_ulamek(a, b):
    nwd_value = nwd(a, b)
    a_prosty = a // nwd_value
    b_prosty = b // nwd_value
    return a_prosty, b_prosty

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
#Gdzie a,b > 0

ulamek = uproszony_ulamek(a, b)


print(f"NWW({a}, {b}) = {nww(a, b)}")
print(f"Ułamek {a}/{b} w najprostszej postaci to {ulamek[0]}/{ulamek[1]}")