#include <iostream>
#include <stdexcept>
using namespace std;
class CFraction
{
    int numerator;
    int denominator;
public:
    CFraction() : numerator(0), denominator(1) {}
    CFraction(int n, int d) : numerator(n), denominator(d)
    {
        if (d == 0) throw invalid_argument("Mianownik nie moze byc zerem");
    }
    void Print() const { cout << numerator << '/' << denominator << '\n'; }
};
int main()
{
    CFraction a(1, 2), b;
    a.Print(); b.Print();
}
