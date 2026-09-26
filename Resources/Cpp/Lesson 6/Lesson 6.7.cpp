#include <iostream>
using namespace std;

struct Example
{
    int a{};
    char b[10]{};
    float c{};
    double* p = nullptr;
    Example* w = nullptr; // wskaznik do wlasnego typu jest dozwolony
    Example* tp[10]{};
    // Example obiekt;     // blad: typ niekompletny, nieskonczona rekurencja rozmiaru
    // Example tablica[10]; // ten sam problem
};

int main()
{
    Example pierwszy{}, drugi{};
    drugi.a = 42;
    pierwszy.w = &drugi;
    pierwszy.tp[0] = &drugi;
    cout << pierwszy.w->a << ' ' << pierwszy.tp[0]->a << '\n';
}
