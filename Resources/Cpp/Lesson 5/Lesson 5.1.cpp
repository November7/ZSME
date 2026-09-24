#include <iostream>

using namespace std;

int main()
{
    int* liczba = new int(42);
    cout << *liczba << '\n';
    delete liczba;
    liczba = nullptr;
    return 0;
}
