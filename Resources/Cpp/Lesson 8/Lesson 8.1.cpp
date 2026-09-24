#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream plik("lesson_8_1.txt");
    if (!plik)
    {
        cerr << "Nie mozna otworzyc pliku\n";
        return 1;
    }
    plik << "Ala 18\nOla 19\n";
    plik.close();
    if (!plik)
        return 1;
    cout << "Zapisano dane\n";
    return 0;
}
