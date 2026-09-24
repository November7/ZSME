#include <iostream>

using namespace std;

enum class Kierunek
{
    Polnoc,
    Poludnie,
    Wschod,
    Zachod
};

int main()
{
    Kierunek kierunek = Kierunek::Wschod;
    switch (kierunek)
    {
        case Kierunek::Polnoc: cout << "Polnoc\n"; break;
        case Kierunek::Poludnie: cout << "Poludnie\n"; break;
        case Kierunek::Wschod: cout << "Wschod\n"; break;
        case Kierunek::Zachod: cout << "Zachod\n"; break;
    }
    return 0;
}
