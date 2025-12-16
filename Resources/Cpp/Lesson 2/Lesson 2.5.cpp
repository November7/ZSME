#include <iostream>
using namespace std;

int main()
{
    // skok bezwarunkowy goto
    int i = 0;
start: // etykieta
    cout << "Iteracja numer: " << i + 1 << endl;
    i++;
    if (i < 5)
        goto start; // skok do etykiety start
    return 0;
}