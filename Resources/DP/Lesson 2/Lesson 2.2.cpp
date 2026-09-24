#include <iostream>
#include <string>

using namespace std;

int fibonacci(int n, int poziom)
{
    cout << string(poziom * 2, ' ') << "f(" << n << ")\n";
    if (n < 2)
        return n;
    int lewy = fibonacci(n - 1, poziom + 1);
    int prawy = fibonacci(n - 2, poziom + 1);
    return lewy + prawy;
}

int main()
{
    int wynik = fibonacci(4, 0);
    cout << wynik << '\n';
    return 0;
}
