#include <iostream>
using namespace std;

int main()
{
    int a = 15;
    int* wsk = &a;

    cout << "Wartosc zmiennej: " << a << endl;
    cout << "Adres zmiennej: " << &a << endl;
    cout << "Wartosc przez wskaznik: " << *wsk << endl;

    return 0;
}