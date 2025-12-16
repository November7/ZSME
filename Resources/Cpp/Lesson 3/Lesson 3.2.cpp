#include <iostream>
using namespace std;

//definicja funkcji przyjmującej dwa parametry typu int i wyświetlającą ich sumę
void suma(int a, int b)
{
    cout << "Suma " << a << " i " << b << " wynosi: " << a + b << endl;
}

int main()
{
    int x = 5;
    int y = 10;
    //wywołanie funkcji suma z argumentami x i y
    suma(x, y);    
    return 0;
}