#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int plecak(const vector<int>& wagi, const vector<int>& wartosci, int pojemnosc)
{
    int n = static_cast<int>(wagi.size());
    vector<vector<int>> dp(n + 1, vector<int>(pojemnosc + 1, 0));
    for (int i = 1; i <= n; ++i)
        for (int w = 0; w <= pojemnosc; ++w)
        {
            dp[i][w] = dp[i - 1][w];
            if (wagi[i - 1] <= w)
                dp[i][w] = max(dp[i][w],
                    dp[i - 1][w - wagi[i - 1]] + wartosci[i - 1]);
        }
    return dp[n][pojemnosc];
}

int main()
{
    cout << plecak({2, 3, 4, 5}, {3, 4, 5, 6}, 5) << '\n';
    cout << plecak({2, 3}, {3, 4}, 0) << '\n';
    cout << plecak({}, {}, 5) << '\n';
    return 0;
}
