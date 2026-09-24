#include <iostream>
#include <fstream>
#include <array>

using namespace std;

int main()
{
    const array<unsigned char, 4> dane{0, 42, 128, 255};
    {
        ofstream zapis("lesson_8_5.bin", ios::binary);
        zapis.write(reinterpret_cast<const char*>(dane.data()), dane.size());
        zapis.close();
        if (!zapis)
            return 1;
    }
    array<unsigned char, 4> wynik{};
    ifstream odczyt("lesson_8_5.bin", ios::binary);
    if (!odczyt.read(reinterpret_cast<char*>(wynik.data()), wynik.size()))
        return 1;
    for (unsigned char bajt : wynik)
        cout << static_cast<int>(bajt) << ' ';
    cout << '\n';
    return 0;
}
