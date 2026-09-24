#include <iostream>
#include <string>

using namespace std;

template <typename T>
class Pudelko
{
    T wartosc;

public:
    explicit Pudelko(const T& poczatkowa) : wartosc(poczatkowa) {}

    const T& pobierz() const
    {
        return wartosc;
    }
};

int main()
{
    Pudelko<int> liczba(42);
    Pudelko<string> tekst("C++");
    cout << liczba.pobierz() << ' ' << tekst.pobierz() << '\n';
    return 0;
}
