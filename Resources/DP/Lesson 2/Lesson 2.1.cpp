#include <iostream>

using namespace std;

long long fibonacci(int n)
{
    if (n < 2)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main()
{
    for (int n = 0; n <= 10; ++n)
        cout << n << ' ' << fibonacci(n) << '\n';
    return 0;
}
