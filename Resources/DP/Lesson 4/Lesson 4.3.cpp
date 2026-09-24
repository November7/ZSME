#include <iostream>
#include <vector>
#include <initializer_list>

using namespace std;

long long fibonacci(int n, vector<long long>& memo)
{
    if (memo[n] != -1)
        return memo[n];
    if (n < 2)
        return memo[n] = n;
    return memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
}

long long tabulacja(int n)
{
    vector<long long> dp(n + 1, 0);
    if (n >= 1)
        dp[1] = 1;
    for (int i = 2; i <= n; ++i)
        dp[i] = dp[i - 1] + dp[i - 2];
    return dp[n];
}

int main()
{
    for (int n : {0, 1, 2, 10, 40})
    {
        vector<long long> memo(n + 1, -1);
        cout << n << ' ' << fibonacci(n, memo) << ' ' << tabulacja(n) << '\n';
    }
    return 0;
}
