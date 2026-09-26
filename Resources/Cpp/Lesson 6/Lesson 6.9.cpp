#include <iostream>
using namespace std;

struct PB { unsigned char a : 5; unsigned char b : 3; };
struct PB1 { unsigned char a : 7, b : 7, c : 1, d : 1; };
struct PB2 { unsigned char a : 7, d : 1, b : 7, c : 1; };
struct PB3
{
    unsigned char a : 7;
    unsigned char : 1; // pole anonimowe
    unsigned char : 5; // pole anonimowe
    unsigned char d : 3;
};

int main()
{
    PB x{};
    x.a = 31;
    x.b = 7;
    PB3 y{};
    y.a = 127;
    y.d = 7;
    cout << "PB: " << sizeof(PB) << ", wartosci: " << +x.a << ' ' << +x.b << '\n';
    cout << "PB1: " << sizeof(PB1) << ", PB2: " << sizeof(PB2) << '\n';
    cout << "PB3: " << sizeof(PB3) << ", wartosci: " << +y.a << ' ' << +y.d << '\n';
    // Upakowanie i rozmiary zaleza od kompilatora i platformy.
}
