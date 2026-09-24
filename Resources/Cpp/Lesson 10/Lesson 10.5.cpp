#include <iostream>
#include <string>

using namespace std;

template <typename T>
struct Opis
{
    static string nazwa()
    {
        return "Inny typ";
    }
};

template <>
struct Opis<int>
{
    static string nazwa()
    {
        return "Liczba calkowita";
    }
};

int main()
{
    cout << Opis<int>::nazwa() << '\n';
    cout << Opis<double>::nazwa() << '\n';
    return 0;
}
