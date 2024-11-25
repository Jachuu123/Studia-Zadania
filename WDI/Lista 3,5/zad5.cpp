#include <iostream>

int main() {
    int a, b;

    std::cout << "Podaj liczby a i b (a < b): ";
    std::cin >> a >> b;

    if (a <= 0 || b <= 0 || a >= b) {
        std::cout << "Liczby musz¹ byæ dodatnie, a < b." << std::endl;
        return 1;
    }

    // Tablica do przechowywania pozycji reszt
    const int MAX_B = 256; // Zak³adamy maksymaln¹ wartoœæ b jako 255
    int remainders[MAX_B];

    // Inicjalizacja tablicy
    for (int i = 0; i < MAX_B; i++) {
        remainders[i] = -1; // -1 oznacza, ¿e reszta jeszcze nie wyst¹pi³a
    }

    int remainder = a;
    int position = 0;
    int period = 0;

    // Obliczanie u³amka
    while (remainder != 0) {
        if (remainders[remainder] != -1) {
            // Znaleziono resztê, co oznacza okres
            period = position - remainders[remainder];
            break;
        }

        // Zapisz pozycjê reszty
        remainders[remainder] = position;

        // Oblicz now¹ resztê
        remainder = (remainder * 2) % b;
        position++;
    }

    // Sprawdzenie skoñczonoœci
    if (remainder == 0) {
        period = 0; // Skoñczona reprezentacja
    }

    // Wynik
    std::cout << "Okres binarnej reprezentacji u³amka " << a << "/" << b << ": " << period << std::endl;

    return 0;
}

