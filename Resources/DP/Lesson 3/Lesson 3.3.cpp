#include <iostream>
#include <vector>

using namespace std;

long long fibonacci(int n, vector<long long>& memo, int& stany)
{
    if (memo[n] != -1)
        return memo[n];
    ++stany;
    if (n < 2)
        return memo[n] = n;
    long long a = fibonacci(n - 1, memo, stany);
    long long b = fibonacci(n - 2, memo, stany);
    return memo[n] = a + b;
}

int main()
{
    for (int n = 10; n <= 40; n += 10)
    {
        vector<long long> memo(n + 1, -1);
        int stany = 0;
        long long wynik = fibonacci(n, memo, stany);
        cout << n << ' ' << wynik << ' ' << stany << '\n';
    }
    return 0;
}
