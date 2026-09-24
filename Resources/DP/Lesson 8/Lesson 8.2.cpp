#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<vector<int>> koszt{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
    int wiersze = static_cast<int>(koszt.size());
    int kolumny = static_cast<int>(koszt[0].size());
    vector<vector<int>> dp(wiersze, vector<int>(kolumny, 0));
    dp[0][0] = koszt[0][0];
    for (int i = 1; i < wiersze; ++i)
        dp[i][0] = dp[i - 1][0] + koszt[i][0];
    for (int j = 1; j < kolumny; ++j)
        dp[0][j] = dp[0][j - 1] + koszt[0][j];
    for (int i = 1; i < wiersze; ++i)
        for (int j = 1; j < kolumny; ++j)
            dp[i][j] = koszt[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
    cout << dp.back().back() << '\n';
    return 0;
}
