#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream odczyt("dane.txt");

    if (!odczyt)
    {
        cout << "Nie mozna otworzyc pliku" << endl;
        return 1;
    }

    string linia;

    while (getline(odczyt, linia))
    {
        cout << linia << endl;
    }

    odczyt.close();
    return 0;
}
