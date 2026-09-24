#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maksymalnaSuma(const vector<int>& liczby)
{
    int n = static_cast<int>(liczby.size());
    vector<int> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i)
    {
        int wez = liczby[i - 1] + (i >= 2 ? dp[i - 2] : 0);
        dp[i] = max(dp[i - 1], wez);
    }
    return dp[n];
}

int main()
{
    cout << maksymalnaSuma({2, 7, 9, 3, 1}) << '\n';
    cout << maksymalnaSuma({-5, -2}) << '\n';
    cout << maksymalnaSuma({}) << '\n';
    return 0;
}
