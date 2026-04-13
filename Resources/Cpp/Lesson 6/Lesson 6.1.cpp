#include <iostream>
using namespace std;

struct Uczen
{
    char imie[20];
    int wiek;
    float srednia;
};

int main()
{
    Uczen u = {"Ola", 16, 4.75f};

    cout << u.imie << endl;
    cout << u.wiek << endl;
    cout << u.srednia << endl;

    return 0;
}