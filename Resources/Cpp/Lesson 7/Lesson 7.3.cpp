#include <iostream>

using namespace std;

class Prostokat
{
    double szerokosc;
    double wysokosc;

public:
    Prostokat() : Prostokat(1, 1) {}
    explicit Prostokat(double bok) : Prostokat(bok, bok) {}
    Prostokat(double a, double b) : szerokosc(a), wysokosc(b) {}

    double pole() const
    {
        return szerokosc * wysokosc;
    }
};

int main()
{
    Prostokat a;
    Prostokat b(3);
    Prostokat c(3, 4);
    cout << a.pole() << ' ' << b.pole() << ' ' << c.pole() << '\n';
    return 0;
}
