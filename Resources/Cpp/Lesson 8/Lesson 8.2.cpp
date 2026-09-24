#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    {
        ofstream zapis("lesson_8_2.txt");
        if (!(zapis << "Pierwszy wiersz\nDrugi wiersz\n"))
            return 1;
    }
    ifstream plik("lesson_8_2.txt");
    if (!plik)
        return 1;
    string wiersz;
    while (getline(plik, wiersz))
        cout << wiersz << '\n';
    return plik.bad() ? 1 : 0;
}
