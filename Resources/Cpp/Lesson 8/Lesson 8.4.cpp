#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream plik("lesson_8_4.txt", ios::app);
    if (!plik)
        return 1;
    plik << "Nowy wpis\n";
    plik.close();
    if (!plik)
        return 1;
    cout << "Dopisano wpis\n";
    return 0;
}
