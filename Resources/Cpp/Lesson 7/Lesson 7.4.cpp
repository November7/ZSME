#include <iostream>
using namespace std;

class Konto
{
private:
    double saldo;

public:
    Konto()
    {
        saldo = 0.0;
    }

    void wplac(double kwota)
    {
        if (kwota > 0)
        {
            saldo += kwota;
        }
    }

    double pobierzSaldo()
    {
        return saldo;
    }
};

int main()
{
    Konto k;
    k.wplac(120.50);
    k.wplac(-10.0);

    cout << k.pobierzSaldo() << endl;

    return 0;
}