#include <iostream>
using namespace std;

int main()
{
    int* liczba = new int;
    *liczba = 25;

    cout << "Wartosc: " << *liczba << endl;

    delete liczba;
    return 0;
}