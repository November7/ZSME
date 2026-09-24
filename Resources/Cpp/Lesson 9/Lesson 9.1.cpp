#include <iostream>
#include <stdexcept>

using namespace std;

double podziel(double a, double b)
{
    if (b == 0)
        throw invalid_argument("Dzielenie przez zero");
    return a / b;
}

int main()
{
    try
    {
        cout << podziel(10, 2) << '\n';
        cout << podziel(10, 0) << '\n';
    }
    catch (const invalid_argument& blad)
    {
        cout << blad.what() << '\n';
    }
    return 0;
}
