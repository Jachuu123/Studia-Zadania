from itertools import combinations_with_replacement
from collections import Counter

words = set([line.strip() for line in open('words.txt', 'r', encoding='utf-8').readlines()])

def find_triplets(name):
    name = name.replace(" ", "").lower()
    name_hash = Counter(name) #ilość wystąpień liter w słowie

    words_hash = [s for s in words if not (Counter(s) - name_hash)]

    result = set()

    # Szukanie trojek
    for first, second, third in combinations_with_replacement(words_hash, 3):
        combined = first + second + third
        if Counter(combined) == name_hash:
            result.add(tuple(sorted([first, second, third])))

    return result

triplets = find_triplets("Bolesław Prus")

# Drukowanie wyników
for triplet in sorted(triplets):
    print(triplet)