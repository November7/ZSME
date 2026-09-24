#include <iostream>

using namespace std;

int main()
{
    int liczba = 10;
    int* wskaznik = &liczba;
    cout << *wskaznik << '\n';
    *wskaznik = 25;
    cout << liczba << '\n';
    return 0;
}
