#include <iostream>
using namespace std;
// przeciążanie funkcji suma dla różnych typów danych
int suma(int a, int b)
{
   return a + b; 
}

double suma(double a, double b)
{
    return a + b;
}

int main()
{
    int x = 5;
    int y = 10;
    cout << "Suma int: " << suma(x, y) << endl;
    
    double m = 5.5;
    double n = 10.3;
    cout << "Suma double: " << suma(m, n) << endl;

    // niejednoznaczne wywołanie funkcji suma
    // argumenty różnych typów - kompilator nie wie, której wersji funkcji użyć
    // cout << "Suma mieszana: " << suma(x, n) << endl; // błąd kompilacji

    return 0;
}