#include <iostream>
using namespace std;

void Hello()
{
    cout << "Hello\n";
}

int Potega2(int n) // przyklad dla niewielkich wartosci
{
    return n * n;
}

void Dzielenie(int a, int b)
{
    if (b == 0)
    {
        cout << "Nie wolno dzielic przez zero!\n";
        return; // konczy funkcje void, nie zwraca wartosci
    }
    cout << a / b << '\n'; // dzielenie calkowite
}

int main()
{
    Hello();
    cout << Potega2(5) << '\n';
    Dzielenie(10, 2);
    Dzielenie(10, 0);
}
