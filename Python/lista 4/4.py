def generate_primes(n):
    arr = [a for a in range(2, n+1)]
    for i in range(2, n+1):
        for item in arr:
            if item % i == 0 and item != i:
                arr[arr.index(item)] = 0
    return arr


def is_palindrome(n):
    num = str(n)
    for i in range(len(num) // 2):
        if num[i] != num[-1-i]:
            return False
    return True

def palindromes(a,b):
    primes = generate_primes(b)
    for i in range(a, b+1):
        if is_palindrome(i) and i in primes:
            print(i)

palindromes(10,1000)
