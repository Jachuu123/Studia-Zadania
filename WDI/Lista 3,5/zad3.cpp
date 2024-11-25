#include <iostream>
#include <string>
#include <math.h>

std::string u2Representation(int n, int k) {
    // Obliczenie minimalnej i maksymalnej wartoœci dla k-bitowej liczby w U2
    int min = -1 * (1 << (k - 1));
    int max = (1 << (k - 1)) - 1;

    // Sprawdzenie, czy liczba mieœci siê w zakresie
    if (n < min || n > max) {
        return "Liczba nie miesci sie w zakresie dla k-bitowego U2";
    }

    // Przekszta³cenie liczby do postaci dodatniej, jeœli jest ujemna
    unsigned int u2Value;
    if (n >= 0) {
        u2Value = n;
    } else {
        u2Value = static_cast<unsigned int>(pow(2, k) + n);
    }

    // Konwersja liczby do postaci binarnej
    std::string result = "";
    for (int i = 0; i < k; ++i) {
        result = (u2Value % 2 == 0 ? "0" : "1") + result;
        u2Value /= 2;
    }

    return result;
}

int main() {
    int n, k;
    std::cout << "Podaj liczbe calkowita n: ";
    std::cin >> n;
    std::cout << "Podaj liczbe bitow k: ";
    std::cin >> k;

    std::string result = u2Representation(n, k);
    std::cout << "Reprezentacja liczby " << n << " w kodzie U2 na " << k << " bitach: " << result << std::endl;

    return 0;
}
