#include <iostream>
using namespace std;

class Licznik
{
public:
    Licznik()
    {
        cout << "Konstruktor" << endl;
    }

    ~Licznik()
    {
        cout << "Destruktor" << endl;
    }
};

int main()
{
    Licznik obiekt;
    return 0;
}