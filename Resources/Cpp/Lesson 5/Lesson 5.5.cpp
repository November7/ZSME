#include <iostream>
#include <new>
using namespace std;

int main()
{
    int rozmiar{};
    cout << "Podaj rozmiar tablicy (1-10000): ";
    if (!(cin >> rozmiar) || rozmiar < 1 || rozmiar > 10000)
        return 1;
    try
    {
        int* p = new int[rozmiar]{}; // wartosci poczatkowe: zera
        for (int i = 0; i < rozmiar; ++i)
            p[i] = i;
        cout << "Pierwszy: " << p[0] << ", ostatni: " << p[rozmiar - 1] << '\n';
        delete[] p;
    }
    catch (const bad_alloc&)
    {
        cerr << "Nieudana alokacja tablicy\n";
        return 2;
    }
}
