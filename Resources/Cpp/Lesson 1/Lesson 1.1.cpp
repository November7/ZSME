#include <iostream>
using namespace std;

int main()
{
    int a;
    cout << "Podaj liczbę całkowitą: ";
    cin >> a;
    if (a % 2 == 0) 
    {
        cout << "Liczba " << a << " jest parzysta." << endl;
    }
    return 0;
}