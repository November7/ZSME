#include <iostream>
#include <algorithm>
#include <utility>
#include <stdexcept>
#include <cstddef>
using namespace std;

class CArray
{
    size_t n = 0;
    char* p = nullptr;
public:
    CArray() = default;
    explicit CArray(size_t rozmiar) : n(rozmiar), p(n ? new char[n]{} : nullptr) {}
    CArray(const CArray& org) : CArray(org.n)
    {
        if (n) copy_n(org.p, n, p);
    }
    CArray& operator=(const CArray& org)
    {
        if (this != &org)
        {
            // Najpierw tworzymy kopie. Jesli new zglosi wyjatek,
            // dotychczasowa zawartosc obiektu pozostanie niezmieniona.
            CArray kopia(org);
            swap(n, kopia.n);
            swap(p, kopia.p);
        } // destruktor kopii zwalnia poprzednia pamiec
        return *this;
    }
    ~CArray() { delete[] p; }
    size_t size() const { return n; }
    char& at(size_t i)
    {
        if (i >= n) throw out_of_range("Indeks poza zakresem");
        return p[i];
    }
};
CArray Example(CArray arg) { return arg; }
int main()
{
    CArray a;
    CArray b(10);
    b.at(0) = 'A';
    CArray c(b);
    c.at(0) = 'B';
    cout << b.at(0) << ' ' << c.at(0) << '\n'; // niezalezne tablice
    a = Example(b);
    cout << a.size() << ' ' << a.at(0) << '\n';
    a = a; // poprawne samoprzypisanie
    a = CArray{}; // zwolnienie poprzedniej tablicy, przypisanie pustej
    cout << a.size() << '\n';
}
