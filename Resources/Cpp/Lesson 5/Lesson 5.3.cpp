#include <iostream>
#include <memory>

using namespace std;

int main()
{
    int wiersze = 2, kolumny = 3;
    auto macierz = make_unique<unique_ptr<int[]>[]>(wiersze);
    for (int i = 0; i < wiersze; ++i)
        macierz[i] = make_unique<int[]>(kolumny);
    for (int i = 0; i < wiersze; ++i)
    {
        for (int j = 0; j < kolumny; ++j)
        {
            macierz[i][j] = i * kolumny + j;
            cout << macierz[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}
