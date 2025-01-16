def ceasar(s, k, alphabet):
    n = len(alphabet)
    shifted = {char: alphabet[(i + k) % n] for i, char in enumerate(alphabet)}
    return ''.join(shifted.get(char, char) for char in s)


def find_longest_cesarskie_pairs(words, alphabet):
    # Sortowanie słów malejąco według długości
    words.sort(key=len, reverse=True)

    # Grupowanie słów według długości
    length_groups = {}
    for word in words:
        length = len(word)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(word)

    # Iteracja po grupach zaczynając od najdłuższych
    for length in sorted(length_groups.keys(), reverse=True):
        group = length_groups[length]
        word_set = set(group)  # Przechowujemy słowa jako zestaw dla szybkiego sprawdzania
        cesarskie_pairs = []

        for word in group:
            for k in range(1, len(alphabet)):  # Sprawdzamy wszystkie przesunięcia
                encrypted = ceasar(word, k, alphabet)
                if encrypted in word_set and encrypted != word:
                    cesarskie_pairs.append((word, encrypted))

        # Jeśli znajdziemy pary, zwróć je natychmiast
        if cesarskie_pairs:
            return cesarskie_pairs

    return []  # Brak par cesarskich


def load_words_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


# Przykład działania
if __name__ == "__main__":
    alphabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

    try:
        words = load_words_from_file('words.txt')
        result = find_longest_cesarskie_pairs(words, alphabet)

        if result:
            print("Najdłuższe pary cesarskie:")
            for pair in result:
                print(pair)
        else:
            print("Nie znaleziono par cesarskich.")
    except FileNotFoundError:
        print("Nie znaleziono pliku 'words.txt'. Upewnij się, że plik istnieje w tym samym folderze, co skrypt.")
