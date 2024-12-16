import random


def random_perm(n):
    numbers = [num for num in range(n)]
    returned = []
    while len(numbers) > 0:
        item = random.choice(list(numbers))
        returned.append(item)
        numbers.remove(item)
    return returned


## Algorytm szybkiego tasowania Fishera-Yatesa (źródło https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)

def random_perm_two(n):
    numbers = [i for i in range(n)]
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(random_perm(10))
print(random_perm(10))
print(random_perm(10))
print(random_perm(10))
print(random_perm(10))


print(random_perm_two(10**6))