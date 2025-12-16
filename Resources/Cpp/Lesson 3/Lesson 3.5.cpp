#include <iostream>
using namespace std;

//funkcja obliczająca potęgę liczby (iteracyjnie)
int potega(int podstawa, int wykladnik)
{
    int wynik = 1;
    for (int i = 0; i < wykladnik; i++)
    {
        wynik *= podstawa;
    }
    return wynik;
}

//funkcja obliczająca potęgę liczby (rekurencyjnie)
int potegaRek(int podstawa, int wykladnik)
{
    if (wykladnik == 0)
        return 1;
    else
        return podstawa * potegaRek(podstawa, wykladnik - 1);
}

int main()
{
    int podstawa = 2;
    int wykladnik = 10;
    cout << podstawa << " ^ " << wykladnik << " = " << potega(podstawa, wykladnik) << endl;
    podstawa = 3;
    wykladnik = 5;
    cout << podstawa << " ^ " << wykladnik << " = " << potegaRek(podstawa, wykladnik) << endl;
    return 0;
}