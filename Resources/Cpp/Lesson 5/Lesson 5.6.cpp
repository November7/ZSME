#include <iostream>
#include <new>
using namespace std;

int main()
{
    int n{}, m{};
    cout << "Podaj liczbe wierszy i kolumn (1-100): ";
    if (!(cin >> n >> m) || n < 1 || n > 100 || m < 1 || m > 100)
        return 1;

    int** p = nullptr;
    int utworzone = 0;
    try
    {
        p = new int*[n]{};
        for (; utworzone < n; ++utworzone)
            p[utworzone] = new int[m]{};
    }
    catch (const bad_alloc&)
    {
        // Jesli zabraknie pamieci, usuwamy wczesniej utworzone wiersze.
        for (int i = 0; i < utworzone; ++i)
            delete[] p[i];
        delete[] p;
        cerr << "Nieudana alokacja macierzy\n";
        return 2;
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            p[i][j] = i * m + j;
            cout << p[i][j] << ' ';
        }
        cout << '\n';
    }
    for (int i = 0; i < n; ++i)
        delete[] p[i];
    delete[] p;
}
