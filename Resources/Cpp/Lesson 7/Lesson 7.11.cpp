#include <iostream>
using namespace std;
class Baza
{
    int prywatne = 1;
protected:
    int chronione = 2;
public:
    int publiczne = 3;
    int pobierzPrywatne() const { return prywatne; }
};
class Publiczna : public Baza
{
public:
    void pokaz() const
    {
        cout << pobierzPrywatne() << ' ' << chronione << ' ' << publiczne << '\n';
        // cout << prywatne; // blad: brak bezposredniego dostepu
    }
};
class Chroniona : protected Baza
{
public:
    void pokaz() const { cout << chronione << ' ' << publiczne << '\n'; }
};
class Prywatna : private Baza
{
public:
    void pokaz() const { cout << chronione << ' ' << publiczne << '\n'; }
};
int main()
{
    Publiczna a; Chroniona b; Prywatna c;
    a.pokaz(); b.pokaz(); c.pokaz();
    cout << a.publiczne << '\n';
    // cout << a.chronione; // blad: protected
    // cout << b.publiczne; // blad: dziedziczenie protected
    // cout << c.publiczne; // blad: dziedziczenie private
}
