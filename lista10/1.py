def ceasar(s, k):
    # Polski alfabet
    alphabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    n = len(alphabet)

    # Tworzenie słownika mapującego litery
    shifted_alphabet = alphabet[k % n:] + alphabet[:k % n]
    mapping = dict(zip(alphabet, shifted_alphabet))

    # Szyfrowanie tekstu
    return ''.join(mapping.get(char, char) for char in s)


# Przykład użycia
if __name__ == "__main__":
    word = "wesołychświąt"
    key = 3
    print("Szyfrogram:", ceasar(word, key))
