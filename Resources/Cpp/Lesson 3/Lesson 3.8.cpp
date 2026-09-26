#include <iostream>
#include <cstddef>
using namespace std;

int suma(int a, int b) { return a + b; }
int suma(int a, int b, int c) { return a + b + c; }
int suma(const int t[], size_t n)
{
    int wynik = 0;
    for (size_t i = 0; i < n; ++i)
        wynik += t[i];
    return wynik;
}

int main()
{
    int liczby[]{1, 2, 3, 4};
    cout << suma(4, 5) << '\n';
    cout << suma(4, 5, 6) << '\n';
    cout << suma(liczby, 4) << '\n';
    // cout << suma(1, 2, 3, 4); // blad: brak wersji z czterema liczbami
    // int suma(int, int); double suma(int, int);
    // Te dwie deklaracje nie moga wspolistniec: inny wynik nie wystarcza.
}
