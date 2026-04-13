#include <iostream>
using namespace std;

class Zwierze
{
public:
    void jedz()
    {
        cout << "Zwierze je" << endl;
    }
};

class Pies : public Zwierze
{
public:
    void szczekaj()
    {
        cout << "Hau hau" << endl;
    }
};

int main()
{
    Pies p;
    p.jedz();
    p.szczekaj();

    return 0;
}