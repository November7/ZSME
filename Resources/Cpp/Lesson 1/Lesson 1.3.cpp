#include <iostream>
using namespace std;

int main()
{
    int a;
    cout << "Podaj liczbę całkowitą: ";
    cin >> a;
    if (a > 0) 
    {
        cout << "Liczba " << a << " jest dodatnia." << endl;
    }
    else if (a < 0) // zagnieżdżona instrukcja warunkowa
    {
        cout << "Liczba " << a << " jest ujemna." << endl;
    }
    else
    {
        cout << "Liczba jest równa zero." << endl;
    }
    return 0;
}