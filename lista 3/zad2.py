from math import sqrt, floor

def isPrime(a):
    n = int(a)
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_numbers():
    nums = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                nums.append('7'*7 + str(i) + str(j) + str(k))
                if i != 0:
                    nums.append(str(i) + '7'*7 + str(j) + str(k))
                    if j != 0:
                        nums.append(str(i) + str(j) + '7'*7 + str(k))
                        if k != 0:
                            nums.append(str(i) + str(j) + str(k) + '7'*7)

    return set(nums)

    
counter = 0

for num in generate_numbers():
    if isPrime(num):
        counter+=1

print('Takich liczb jest:', counter)

