#include <iostream>
#include <vector>
#include <stdexcept>
#include <exception>

using namespace std;

int main()
{
    vector<int> liczby{10, 20};
    try
    {
        cout << liczby.at(5) << '\n';
    }
    catch (const out_of_range& blad)
    {
        cout << "Indeks poza zakresem: " << blad.what() << '\n';
    }
    catch (const exception& blad)
    {
        cout << blad.what() << '\n';
    }
    return 0;
}
