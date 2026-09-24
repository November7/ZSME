#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> wagi{2, 3, 4, 5};
    vector<int> wartosci{3, 4, 5, 6};
    int n = static_cast<int>(wagi.size()), pojemnosc = 5;
    vector<vector<int>> dp(n + 1, vector<int>(pojemnosc + 1, 0));
    for (int i = 1; i <= n; ++i)
        for (int w = 0; w <= pojemnosc; ++w)
        {
            dp[i][w] = dp[i - 1][w];
            if (wagi[i - 1] <= w)
                dp[i][w] = max(dp[i][w],
                    dp[i - 1][w - wagi[i - 1]] + wartosci[i - 1]);
        }
    vector<int> wybrane;
    int w = pojemnosc;
    for (int i = n; i > 0; --i)
        if (dp[i][w] != dp[i - 1][w])
        {
            wybrane.push_back(i - 1);
            w -= wagi[i - 1];
        }
    reverse(wybrane.begin(), wybrane.end());
    cout << dp[n][pojemnosc] << '\n';
    for (int i : wybrane)
        cout << i << ' ' << wagi[i] << ' ' << wartosci[i] << '\n';
    return 0;
}
