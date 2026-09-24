#include <iostream>

using namespace std;

class Konto
{
    int saldo = 0;

public:
    bool wplac(int kwota)
    {
        if (kwota <= 0)
            return false;
        saldo += kwota;
        return true;
    }

    bool wyplac(int kwota)
    {
        if (kwota <= 0 || kwota > saldo)
            return false;
        saldo -= kwota;
        return true;
    }

    int pobierzSaldo() const
    {
        return saldo;
    }
};

int main()
{
    Konto konto;
    konto.wplac(100);
    cout << boolalpha << konto.wyplac(30) << '\n';
    cout << konto.wyplac(200) << '\n';
    cout << konto.pobierzSaldo() << '\n';
    return 0;
}
