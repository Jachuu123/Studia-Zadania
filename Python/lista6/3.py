def dividers(n):
    result = set()
    i = 1
    while n >= i:
        if n % i == 0:
            result.add(i)
            n /= i
            i = 2
        else:
            i+=1
    result.remove(1)
    return result

print(dividers(340))