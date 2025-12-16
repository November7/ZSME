#include <iostream>
using namespace std;

//definicja funkcji przyjmującej dwa parametry typu int i zwracającej ich sumę
int suma(int a, int b)
{
    return a + b;
}

int main()
{
    int x = 5;
    int y = 10;
    //wywołanie funkcji suma z argumentami x i y
    int wynik = suma(x, y);    
    cout << "Suma " << x << " i " << y << " wynosi: " << wynik << endl;
    return 0;
}