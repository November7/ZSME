#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> liczby{2, 7, 9, 3, 1};
    int n = static_cast<int>(liczby.size());
    vector<int> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i)
        dp[i] = max(dp[i - 1], liczby[i - 1] + (i >= 2 ? dp[i - 2] : 0));
    vector<int> indeksy;
    for (int i = n; i > 0;)
    {
        if (dp[i] == dp[i - 1])
            --i;
        else
        {
            indeksy.push_back(i - 1);
            i -= 2;
        }
    }
    reverse(indeksy.begin(), indeksy.end());
    cout << dp[n] << '\n';
    for (int i : indeksy)
        cout << i << ' ' << liczby[i] << '\n';
    return 0;
}
