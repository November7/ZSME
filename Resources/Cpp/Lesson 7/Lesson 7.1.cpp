#include <iostream>

using namespace std;

class Prostokat
{
public:
    double szerokosc = 0;
    double wysokosc = 0;

    double pole() const
    {
        return szerokosc * wysokosc;
    }
};

int main()
{
    Prostokat prostokat;
    prostokat.szerokosc = 3;
    prostokat.wysokosc = 4;
    cout << prostokat.pole() << '\n';
    return 0;
}
