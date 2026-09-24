#include <iostream>
#include <string>
#include <stdexcept>
#include <exception>

using namespace std;

int odczytaj()
{
    try
    {
        return stoi("abc");
    }
    catch (const invalid_argument&)
    {
        cout << "Niepoprawny zapis liczby\n";
        throw;
    }
}

int main()
{
    try
    {
        cout << odczytaj() << '\n';
    }
    catch (const exception& blad)
    {
        cout << blad.what() << '\n';
    }
    return 0;
}
