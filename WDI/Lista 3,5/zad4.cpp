#include <iostream>

int main() {
    int n = 4; // D�ugo�� bit�w (przyk�ad: 4 bity)

    std::cin >> n;
    int A[n], B[n], result[n];

    // Wczytanie pierwszej liczby
    std::cout << "Podaj cyfry pierwszej liczby (0 lub 1, oddzielone spacj�): ";
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    // Wczytanie drugiej liczby
    std::cout << "Podaj cyfry drugiej liczby (0 lub 1, oddzielone spacj�):   ";
    for (int i = 0; i < n; i++) {
        std::cin >> B[i];
    }

    int carry = 0;

    // Dodawanie
    for (int i = n - 1; i >= 0; i--) {
        int sum = A[i] + B[i] + carry;
        result[i] = sum % 2;  // Zapisz bit wyniku
        carry = sum / 2;       // Oblicz przeniesienie
    }

    // Sprawdzenie przepe�nienia
    if (carry != 0) {
        std::cout << "Przepe�nienie! Wynik przekracza zakres." << std::endl;
    }

    // Wy�wietlenie wyniku
    std::cout << "Wynik dodawania: ";
    for (int i = 0; i < n; i++) {
        std::cout << result[i];
    }
    std::cout << std::endl;

    return 0;
}

