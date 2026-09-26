#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    { // samodzielny przyklad: przygotowanie pliku wejsciowego
        ofstream dane("lesson_8_6_we.txt");
        dane << "Pierwszy wiersz\nDrugi wiersz";
        dane.close();
        if (!dane) return 1;
    }
    ifstream fin("lesson_8_6_we.txt");
    ofstream fout("lesson_8_6_wy.txt", ios::trunc);
    if (!fin || !fout) return 2;
    string wiersz;
    while (getline(fin, wiersz))
        fout << wiersz << '\n';
    if (fin.bad() || !fin.eof()) return 3;
    fout.close();
    if (!fout) return 4;
    cout << "Skopiowano wiersze\n";
    // Kopia tekstowa dopisuje znak nowej linii po kazdym wierszu,
    // nie jest kopia bajt w bajt (zwlaszcza ostatni wiersz).
}
