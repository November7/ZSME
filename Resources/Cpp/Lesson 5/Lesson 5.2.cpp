#include <iostream>
using namespace std;

int main()
{
    int n = 5;
    int* tab = new int[n];

    for (int i = 0; i < n; i++)
    {
        tab[i] = (i + 1) * 10;
    }

    for (int i = 0; i < n; i++)
    {
        cout << tab[i] << " ";
    }
    cout << endl;

    delete[] tab;
    return 0;
}