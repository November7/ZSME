#include <iostream>

using namespace std;

int main()
{
    // // signed / unsigned
    // char c; // typ znakowy, liczba ze znakiem 1B <-128, 127> 1B (8b)
    // short s; // liczba całkowita ze znakiem <-32768, 32767> 2B (16)
    // int x; // liczba całkowita ze znakiem <-2147483648, 2147483647>, int jest 4B (32b)
    // long l; // liczba całkowita ze znakiem <-duzo, duzo> long int jest 4B (32b) / 8B (64b)

    // signed long int x;

    
    // float f; //liczba zmiennoprzecinkowa 4B, ze znakiem
    // double d; //liczba zmiennoprzecinkowa 8B, ze znakiem
    // long double ld; //liczba zmiennoprzecinkowa 8B/10B/12B, ze znakiem

    // bool b; // true / false
    
    // string str;

    int a, b;
    cout << "Podaj liczby " << endl;
    cin >> a >> b;
    cout << "Suma liczb wynosi " << a + b << endl;
    
    cout << "Srednia liczb "<< a <<" i "<< b <<" wynosi " << (a + b) / 2.0 << endl;



    return 0;
}