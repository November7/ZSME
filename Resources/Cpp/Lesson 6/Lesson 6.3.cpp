#include <iostream>

using namespace std;

union Wartosc
{
    int calkowita;
    double rzeczywista;
};

int main()
{
    Wartosc wartosc{};
    wartosc.calkowita = 42;
    cout << wartosc.calkowita << '\n';
    wartosc.rzeczywista = 3.5;
    cout << wartosc.rzeczywista << '\n';
    return 0;
}
