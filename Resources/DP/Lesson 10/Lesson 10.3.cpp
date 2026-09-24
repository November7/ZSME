#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int odleglosc(const string& a, const string& b)
{
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; ++i)
        dp[i][0] = i;
    for (int j = 0; j <= m; ++j)
        dp[0][j] = j;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + (a[i - 1] != b[j - 1])});
    return dp[n][m];
}

int main()
{
    cout << odleglosc("kitten", "sitting") << '\n';
    cout << odleglosc("", "kot") << '\n';
    cout << odleglosc("kot", "kot") << '\n';
    return 0;
}
