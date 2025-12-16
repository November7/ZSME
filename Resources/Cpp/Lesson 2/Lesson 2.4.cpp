#include <iostream>
using namespace std;

int main()
{
    // instrukcja break
    for (int i = 0; i < 20; i++)
    {
        if (i == 5)
        {
            break; // przerywa działanie pętli gdy i równa się 5
        }
        cout << "Iteracja numer: " << i + 1 << endl;
    }

    // instrukcja continue
    for (int i = 0; i < 20; i++)
    {
        if (i % 3 == 0 || i % 4 == 0)
        {
            continue; // pomija resztę kodu w pętli dla liczb podzielnych przez 3 lub 4
        }
        cout << "Liczby które nie zostały pominięte: " << i << endl;
    }
    return 0;
}