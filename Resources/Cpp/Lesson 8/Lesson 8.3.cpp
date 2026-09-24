#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    {
        ofstream zapis("lesson_8_3.txt");
        if (!(zapis << "10 20 30\n"))
            return 1;
    }
    ifstream plik("lesson_8_3.txt");
    if (!plik)
        return 1;
    int liczba;
    int suma = 0;
    while (plik >> liczba)
        suma += liczba;
    if (plik.bad() || !plik.eof())
    {
        cerr << "Blad odczytu\n";
        return 1;
    }
    cout << suma << '\n';
    return 0;
}
