#include <iostream>
#include <stdexcept>
using namespace std;
class CFraction
{
    int numerator;
    int denominator;
public:
    CFraction(int n = 0, int d = 1) : numerator(n), denominator(d)
    {
        if (d == 0) throw invalid_argument("Mianownik nie moze byc zerem");
    }
    void Print() const { cout << numerator << '/' << denominator << '\n'; }
    CFraction operator*(const CFraction& arg) const
    {
        return CFraction(numerator * arg.numerator, denominator * arg.denominator);
    }
    CFraction& operator++() { numerator += denominator; return *this; }
    CFraction& operator--() { numerator -= denominator; return *this; }
    CFraction operator++(int)
    {
        CFraction kopia = *this;
        ++(*this);
        return kopia;
    }
    CFraction operator--(int)
    {
        CFraction kopia = *this;
        --(*this);
        return kopia;
    }
};
int main()
{
    CFraction A(1,2);
    CFraction B(2,3);
    A.Print();
    B.Print();
    CFraction C;
    C = A * B;
    C.Print();
    C++;
    C.Print();
    ++C;
    C.Print();
    C--;
    C.Print();
    --C;
    C.Print();
    /*
    Ponieważ opeatory preinkrementacji i predekrementacji zwracają referencję do oryginalnego obiektu,
    możliwe jest wykonanie poniższej instrukcji
    */
    ++++++++++++++++++C;
    C.Print();
    return 0;
}
