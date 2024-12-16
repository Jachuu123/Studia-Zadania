def parse_hashmap(text):
    result = {}
    for char in text:
        if char not in result:
            result.update({char:1})
        else:
            result[char] += 1
    return result

def is_ukladne(main,predicate):
    letters = parse_hashmap(main)
    for char in predicate:
        if char not in letters:
            return False
        if letters[char] < predicate.count(char):
            return False
    return True



print(is_ukladne('piesek', 'pis'))