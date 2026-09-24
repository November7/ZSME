#include <iostream>

using namespace std;

class Obiekt
{
public:
    Obiekt()
    {
        cout << "Konstruktor\n";
    }

    ~Obiekt()
    {
        cout << "Destruktor\n";
    }
};

int main()
{
    cout << "Poczatek\n";
    {
        Obiekt obiekt;
        cout << "Wewnatrz bloku\n";
    }
    cout << "Koniec\n";
    return 0;
}
