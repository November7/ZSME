#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string lcs(const string& a, const string& b)
{
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (a[i - 1] == b[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
    string wynik;
    int i = n, j = m;
    while (i > 0 && j > 0)
    {
        if (a[i - 1] == b[j - 1])
        {
            wynik += a[i - 1];
            --i;
            --j;
        }
        else if (dp[i - 1][j] >= dp[i][j - 1])
            --i;
        else
            --j;
    }
    reverse(wynik.begin(), wynik.end());
    return wynik;
}

int main()
{
    string wynik = lcs("ABCBDAB", "BDCABA");
    cout << wynik.size() << '\n' << wynik << '\n';
    cout << lcs("", "ABC").size() << '\n';
    return 0;
}
