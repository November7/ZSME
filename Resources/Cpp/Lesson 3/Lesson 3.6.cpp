#include <iostream>
using namespace std;

int suma(int, int); // deklaracja: nazwy parametrow nie sa wymagane

int main()
{
    int a{}, b{};
    cout << "Podaj dwie niewielkie liczby calkowite: ";
    if (!(cin >> a >> b) || a < -1000000 || a > 1000000 || b < -1000000 || b > 1000000)
        return 1;
    cout << suma(a, b) << '\n'; // argumenty aktualne: a i b
    cout << suma(4, 5) << '\n'; // argumenty aktualne: wartosci 4 i 5
}

int suma(int arg_1, int arg_2) // definicja; parametry formalne
{
    return arg_1 + arg_2;
}
