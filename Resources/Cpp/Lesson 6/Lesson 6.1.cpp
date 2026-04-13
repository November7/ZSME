#include <iostream>
using namespace std;

struct Uczen
{
    char imie[20];
    int wiek;
    float srednia;
};

struct Punkt2D
{
    char etykieta;
    int x;
    int y;
};

int main()
{
    Uczen u = {"Ola", 16, 4.75f};

    cout << u.imie << endl;
    cout << u.wiek << endl;
    cout << u.srednia << endl;
    cout << "Rozmiar Uczen: " << sizeof(Uczen) << " bajtow" << endl;
    cout << "Rozmiar Punkt2D: " << sizeof(Punkt2D) << " bajtow" << endl;

    return 0;
}