#include <iostream>

using namespace std;

int fibonacci(int n, int& wywolania)
{
    ++wywolania;
    if (n < 2)
        return n;
    int a = fibonacci(n - 1, wywolania);
    int b = fibonacci(n - 2, wywolania);
    return a + b;
}

int main()
{
    for (int n = 5; n <= 25; n += 5)
    {
        int wywolania = 0;
        int wynik = fibonacci(n, wywolania);
        cout << n << ' ' << wynik << ' ' << wywolania << '\n';
    }
    return 0;
}
