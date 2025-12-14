#include <iostream>

using namespace std;
 
#define JAKAS_STALA_SYMBOLICZNA
#define PI 3.14
#define DWAPI 2*PI
 
int main()
{
    int r;
    cout << "Podaj promien kola: ";
    cin >> r;
    cout << "Pole kola o promieniu " << r << " wynosi: " << PI*r*r << ", a obwod wynosi: " << DWAPI*r << endl;
    return 0;
}