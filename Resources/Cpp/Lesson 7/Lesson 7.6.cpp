#include <iostream>
#include <string>

using namespace std;

class Osoba
{
    string imie;

public:
    explicit Osoba(const string& noweImie) : imie(noweImie) {}

    const string& pobierzImie() const
    {
        return imie;
    }
};

class Uczen : public Osoba
{
    int klasa;

public:
    Uczen(const string& imie, int numer) : Osoba(imie), klasa(numer) {}

    int pobierzKlase() const
    {
        return klasa;
    }
};

int main()
{
    Uczen uczen("Ala", 3);
    cout << uczen.pobierzImie() << ' ' << uczen.pobierzKlase() << '\n';
    return 0;
}
