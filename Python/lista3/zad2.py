import math

def pierwsza(n):
    if n == 1 or n == 2:
        return True

    for i in range(2,int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

print(pierwsza(8))

sied = 7*'7'
tab = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            if a != 0:
                tab.append(str(a)+str(b)+str(c)+sied)
                tab.append(str(a)+str(b)+sied+str(c))
                tab.append(str(a)+sied+str(b)+str(c))
            tab.append(sied+str(a)+str(b)+str(c))
    #print(i)
wyn = set(tab)
tab.sort()

for i in tab:
    print(i)
licznik = 0



for i in wyn:
    if pierwsza(int(i)) == True:
        licznik += 1
print(licznik)