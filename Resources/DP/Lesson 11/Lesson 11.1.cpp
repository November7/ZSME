#include <iostream>
#include <initializer_list>

using namespace std;

long long fibonacci(int n)
{
    if (n == 0)
        return 0;
    long long poprzedni = 0, obecny = 1;
    for (int i = 2; i <= n; ++i)
    {
        long long nastepny = poprzedni + obecny;
        poprzedni = obecny;
        obecny = nastepny;
    }
    return obecny;
}

int main()
{
    for (int n : {0, 1, 2, 10, 40})
        cout << n << ' ' << fibonacci(n) << '\n';
    return 0;
}
