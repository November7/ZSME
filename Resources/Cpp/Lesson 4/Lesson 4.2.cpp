#include <iostream>

using namespace std;

int main()
{
    int liczby[] = {3, 1, 4, 1, 5};
    int suma = 0;
    for (int liczba : liczby)
    {
        suma += liczba;
        cout << liczba << ' ';
    }
    cout << '\n' << suma << '\n';
    return 0;
}
