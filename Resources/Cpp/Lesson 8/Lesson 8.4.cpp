#include <iostream>
#include <fstream>
using namespace std;

struct Rekord
{
    int id;
    float ocena;
};

int main()
{
    Rekord zapis = {7, 4.5f};

    ofstream wyjscie("dane.bin", ios::binary);
    if (!wyjscie)
    {
        cout << "Nie mozna otworzyc pliku do zapisu" << endl;
        return 1;
    }

    wyjscie.write(reinterpret_cast<char*>(&zapis), sizeof(Rekord));
    wyjscie.close();

    Rekord odczyt;
    ifstream wejscie("dane.bin", ios::binary);
    if (!wejscie)
    {
        cout << "Nie mozna otworzyc pliku do odczytu" << endl;
        return 1;
    }

    wejscie.read(reinterpret_cast<char*>(&odczyt), sizeof(Rekord));
    wejscie.close();

    cout << "id: " << odczyt.id << endl;
    cout << "ocena: " << odczyt.ocena << endl;

    return 0;
}
