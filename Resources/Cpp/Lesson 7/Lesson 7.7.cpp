#include <iostream>
using namespace std;

class Figura
{
public:
    virtual void rysuj()
    {
        cout << "Rysuje figure" << endl;
    }
};

class Kolo : public Figura
{
public:
    void rysuj()
    {
        cout << "Rysuje kolo" << endl;
    }
};

int main()
{
    Figura* f;
    Kolo k;

    f = &k;
    f->rysuj();

    return 0;
}