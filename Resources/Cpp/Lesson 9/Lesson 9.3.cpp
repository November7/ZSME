#include <iostream>
#include <stdexcept>

using namespace std;

class BrakSrodkow : public runtime_error
{
public:
    BrakSrodkow() : runtime_error("Brak srodkow na koncie") {}
};

int main()
{
    int saldo = 50;
    int kwota = 80;
    try
    {
        if (kwota > saldo)
            throw BrakSrodkow();
        saldo -= kwota;
    }
    catch (const BrakSrodkow& blad)
    {
        cout << blad.what() << '\n';
    }
    cout << saldo << '\n';
    return 0;
}
