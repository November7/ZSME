#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> liczby;
    liczby.reserve(10);
    liczby.resize(4, 7);
    cout << liczby.size() << ' ' << (liczby.capacity() >= 10) << '\n';
    vector<vector<int>> macierz(2, vector<int>(3, 0));
    macierz[1][2] = 5;
    for (const auto& wiersz : macierz)
    {
        for (int wartosc : wiersz)
            cout << wartosc << ' ';
        cout << '\n';
    }
    return 0;
}
