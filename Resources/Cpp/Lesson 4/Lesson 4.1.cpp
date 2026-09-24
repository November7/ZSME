#include <iostream>

using namespace std;

int main()
{
    int liczby[4] = {10, 20, 30, 40};
    liczby[1] = 25;
    cout << liczby[0] << ' ' << liczby[1] << '\n';
    cout << sizeof(liczby) / sizeof(liczby[0]) << '\n';
    return 0;
}
