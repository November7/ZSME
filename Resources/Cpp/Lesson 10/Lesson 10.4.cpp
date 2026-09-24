#include <iostream>
#include <array>
#include <cstddef>

using namespace std;

template <typename T, size_t N>
T suma(const array<T, N>& liczby)
{
    T wynik{};
    for (const T& liczba : liczby)
        wynik += liczba;
    return wynik;
}

int main()
{
    array<int, 3> liczby{1, 2, 3};
    cout << suma(liczby) << '\n';
    return 0;
}
