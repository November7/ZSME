#include <iostream>
using namespace std;

class Prostokat
{
private:
    int a;
    int b;

public:
    Prostokat()
    {
        a = 1;
        b = 1;
    }

    Prostokat(int bokA, int bokB)
    {
        a = bokA;
        b = bokB;
    }

    int pole()
    {
        return a * b;
    }
};

int main()
{
    Prostokat p1;
    Prostokat p2(4, 6);

    cout << p1.pole() << endl;
    cout << p2.pole() << endl;

    return 0;
}