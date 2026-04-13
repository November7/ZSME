#include <iostream>
using namespace std;

union Liczba
{
    int calkowita;
    float zmiennoprzecinkowa;
};

int main()
{
    Liczba x;

    x.calkowita = 10;
    cout << "int: " << x.calkowita << endl;

    x.zmiennoprzecinkowa = 3.5f;
    cout << "float: " << x.zmiennoprzecinkowa << endl;

    return 0;
}