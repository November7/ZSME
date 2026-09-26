#include <iostream>
using namespace std;
class CExample
{
public:
    void m1() const { cout << "Metoda zdefiniowana w klasie\n"; }
    void m2() const;
};
void CExample::m2() const { cout << "Metoda zdefiniowana poza klasa\n"; }
int main() { CExample obiekt; obiekt.m1(); obiekt.m2(); }
