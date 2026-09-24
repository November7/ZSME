#include <iostream>
#include <vector>

using namespace std;

long long fibonacci(int n)
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
    cout << fibonacci(0) << '\n';
    cout << fibonacci(1) << '\n';
    cout << fibonacci(40) << '\n';
    return 0;
}
