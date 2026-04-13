#include <iostream>
using namespace std;

int main()
{
    int wiersze = 2;
    int kolumny = 3;

    int** macierz = new int*[wiersze];
    for (int i = 0; i < wiersze; i++)
    {
        macierz[i] = new int[kolumny];
    }

    int wartosc = 1;
    for (int i = 0; i < wiersze; i++)
    {
        for (int j = 0; j < kolumny; j++)
        {
            macierz[i][j] = wartosc++;
        }
    }

    for (int i = 0; i < wiersze; i++)
    {
        for (int j = 0; j < kolumny; j++)
        {
            cout << macierz[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < wiersze; i++)
    {
        delete[] macierz[i];
    }
    delete[] macierz;

    return 0;
}