#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int odleglosc(const string& a, const string& b)
{
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    vector<int> dp(m + 1);
    iota(dp.begin(), dp.end(), 0);
    for (int i = 1; i <= n; ++i)
    {
        int przekatna = dp[0];
        dp[0] = i;
        for (int j = 1; j <= m; ++j)
        {
            int poprzedni = dp[j];
            dp[j] = min({dp[j] + 1, dp[j - 1] + 1,
                przekatna + (a[i - 1] != b[j - 1])});
            przekatna = poprzedni;
        }
    }
    return dp[m];
}

int main()
{
    cout << odleglosc("kitten", "sitting") << '\n';
    cout << odleglosc("", "kot") << '\n';
    cout << odleglosc("kot", "kot") << '\n';
    return 0;
}
