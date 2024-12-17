from itertools import combinations
from collections import Counter
words = set([line.strip() for line in open('words.txt', 'r', encoding='utf-8').readlines()])

def find_pairs(name):
    name = name.replace(" ", "").lower()
    name_hash = Counter(name) #słownik zliczający litery w imieniu
    
    words_hash = [s for s in words if not (Counter(s) - name_hash)]
    
    result = set()
    
    for first, second in combinations(words_hash, 2):
        if Counter(first + second) == name_hash:
            result.add(tuple(sorted([first, second])))
    
    return result

pairs = find_pairs("Adam Mickieicz")
    
for pair in sorted(pairs):
    print(pair)
