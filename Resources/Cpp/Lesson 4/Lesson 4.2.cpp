#include <iostream>
using namespace std;

int main()
{
    int liczby[5] = {5, 1, 7, 3, 9};
    int suma = 0;

    for (int i = 0; i < 5; i++)
    {
        suma += liczby[i];
    }

    cout << "Suma: " << suma << endl;

    return 0;
}