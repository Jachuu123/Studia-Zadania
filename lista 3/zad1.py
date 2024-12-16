from math import sqrt, floor

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_happy(n):
    numberAsString = str(n)
    counter = 0
    for i in numberAsString:
        if i == '7':
            counter+=1
            if counter == 3:
                return True
        else:
            counter = 0
    return False
        
counter = 0
for i in range(1, 100_000):
    if is_prime(i) and is_happy(i):
        print(i)
        counter+=1

print('Takich liczb jest:', counter)