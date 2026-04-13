#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream zapis("dane.txt");
    zapis << "Ala" << endl;
    zapis << "Kot" << endl;
    zapis.close();

    ifstream odczyt("dane.txt");
    string linia;

    while (getline(odczyt, linia))
    {
        cout << linia << endl;
    }

    odczyt.close();
    return 0;
}