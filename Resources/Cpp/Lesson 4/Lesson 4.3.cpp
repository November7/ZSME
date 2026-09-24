#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char imie[20] = "Ala";
    cout << imie << ' ' << strlen(imie) << '\n';
    imie[0] = 'O';
    cout << imie << '\n';
    return 0;
}
