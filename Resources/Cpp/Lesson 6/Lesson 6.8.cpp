#include <iostream>
#include <cstddef>
using namespace std;

struct Naturalny
{
    char x;
    double y;
};

// Rozszerzenie kompilatorow GCC, Clang i MSVC, a nie wymog standardu C++.
#pragma pack(push, 1)
struct Pakowany
{
    char x;
    double y;
};
#pragma pack(pop) // przywrocenie poprzedniego ustawienia

int main()
{
    cout << "Suma pol: " << sizeof(char) + sizeof(double) << '\n';
    cout << "Naturalny: " << sizeof(Naturalny) << ", offset y: " << offsetof(Naturalny, y) << '\n';
    cout << "Pakowany: " << sizeof(Pakowany) << ", offset y: " << offsetof(Pakowany, y) << '\n';
    // Nie zakladamy z gory rozmiarow 16 i 9: wynik zalezy od implementacji.
}
