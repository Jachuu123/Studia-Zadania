def palindrom_binarny(n):
    zap_bin = ""

    while n > 0:
        zap_bin = f"{str(n%2)}" + zap_bin
        n = n // 2

    for i in range(len(zap_bin)//2 + 1):
        if zap_bin[i] != zap_bin[len(zap_bin)-1-i]:
            return False
        return True

def palindrom_knarny(n,k):
    zap = ""

    while n > 0:
        zap = f"{str(n%k)}" + zap
        n = n // k

    for i in range(len(zap) // 2 + 1):
        if zap[i] != zap[len(zap) - 1 - i]:
            return False
        return True

        #print(zap)
        #print(zap_reverse)

    if zap == zap_reverse:
        return True
    else:
        return False

# n > 0
n = int(input("Podaj n:"))
print(palindrom_binarny(n))
print(palindrom_knarny(1,3))