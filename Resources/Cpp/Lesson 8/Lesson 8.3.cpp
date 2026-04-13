#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream plik("dane.txt", ios::in | ios::out | ios::trunc);

    if (!plik)
    {
        cout << "Nie mozna otworzyc pliku" << endl;
        return 1;
    }

    plik << "Linia 1" << endl;
    plik << "Linia 2" << endl;

    plik.seekg(0);

    string linia;
    while (getline(plik, linia))
    {
        cout << linia << endl;
    }

    plik.close();
    return 0;
}
