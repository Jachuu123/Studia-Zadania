#include <iostream>

int main() {
    int a, b;

    std::cout << "Podaj liczby a i b (a < b): ";
    std::cin >> a >> b;

    if (a <= 0 || b <= 0 || a >= b) {
        std::cout << "Liczby musz� by� dodatnie, a < b." << std::endl;
        return 1;
    }

    // Tablica do przechowywania pozycji reszt
    const int MAX_B = 256; // Zak�adamy maksymaln� warto�� b jako 255
    int remainders[MAX_B];

    // Inicjalizacja tablicy
    for (int i = 0; i < MAX_B; i++) {
        remainders[i] = -1; // -1 oznacza, �e reszta jeszcze nie wyst�pi�a
    }

    int remainder = a;
    int position = 0;
    int period = 0;

    // Obliczanie u�amka
    while (remainder != 0) {
        if (remainders[remainder] != -1) {
            // Znaleziono reszt�, co oznacza okres
            period = position - remainders[remainder];
            break;
        }

        // Zapisz pozycj� reszty
        remainders[remainder] = position;

        // Oblicz now� reszt�
        remainder = (remainder * 2) % b;
        position++;
    }

    // Sprawdzenie sko�czono�ci
    if (remainder == 0) {
        period = 0; // Sko�czona reprezentacja
    }

    // Wynik
    std::cout << "Okres binarnej reprezentacji u�amka " << a << "/" << b << ": " << period << std::endl;

    return 0;
}

