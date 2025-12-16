#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Znaki
    char a = 'a';
    signed char b = -128;
    unsigned char c = 255;

    // Liczby całkowite
    short d = 1234;
    signed short e = -32768;
    unsigned short f = 65535;

    int g = 123456;
    signed int h = -2147483648;
    unsigned int i = 4294967295U;

    long j = 123456789L;
    signed long k = -2147483647L;
    unsigned long l = 4294967295UL;

    long long m = 123456789012345LL;
    signed long long n = -9223372036854775807LL;
    unsigned long long o = 18446744073709551615ULL;

    // Typy zmiennoprzecinkowe
    float p = 3.14f;
    double q = 3.141592653589793;
    long double r = 3.141592653589793238462643383279L;

    // Typy logiczne
    bool s = true;

    // Wskaźnik    
    int* t = &g;

    // Wypisywanie
    cout << left << setw(25) << "Typ" 
         << setw(25) << "Wartość" 
         << setw(15) << "Rozmiar (B)" << endl;
    cout << string(65, '-') << endl;

    cout << setw(25) << "char" << setw(25) << a << sizeof(a) << endl;
    cout << setw(25) << "signed char" << setw(25) << (int)b << sizeof(b) << endl;
    cout << setw(25) << "unsigned char" << setw(25) << (unsigned)c << sizeof(c) << endl;

    cout << setw(25) << "short" << setw(25) << d << sizeof(d) << endl;
    cout << setw(25) << "signed short" << setw(25) << e << sizeof(e) << endl;
    cout << setw(25) << "unsigned short" << setw(25) << f << sizeof(f) << endl;

    cout << setw(25) << "int" << setw(25) << g << sizeof(g) << endl;
    cout << setw(25) << "signed int" << setw(25) << h << sizeof(h) << endl;
    cout << setw(25) << "unsigned int" << setw(25) << i << sizeof(i) << endl;

    cout << setw(25) << "long" << setw(25) << j << sizeof(j) << endl;
    cout << setw(25) << "signed long" << setw(25) << k << sizeof(k) << endl;
    cout << setw(25) << "unsigned long" << setw(25) << l << sizeof(l) << endl;

    cout << setw(25) << "long long" << setw(25) << m << sizeof(m) << endl;
    cout << setw(25) << "signed long long" << setw(25) << n << sizeof(n) << endl;
    cout << setw(25) << "unsigned long long" << setw(25) << o << sizeof(o) << endl;

    cout << fixed << setprecision(15); // 15 miejsc po 'przecinku'

    cout << setw(25) << "float" << setw(25) << p << sizeof(p) << endl;
    cout << setw(25) << "double" << setw(25) << q << sizeof(q) << endl;
    cout << setw(25) << "long double" << setw(25) << r << sizeof(r) << endl;

    cout << setw(25) << "bool" << setw(25) << s << sizeof(s) << endl;

    cout << setw(25) << "int*" << setw(25) << t << sizeof(t) << endl;

    return 0;
}