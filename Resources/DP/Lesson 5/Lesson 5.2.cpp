#include <iostream>
#include <vector>
#include <initializer_list>

using namespace std;

long long schody(int n)
{
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; ++i)
    {
        dp[i] = dp[i - 1];
        if (i >= 2)
            dp[i] += dp[i - 2];
    }
    return dp[n];
}

int main()
{
    for (int n : {0, 1, 2})
        cout << n << ' ' << schody(n) << '\n';
    return 0;
}
