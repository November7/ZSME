#include <iostream>
#include <vector>
#include <string>

using namespace std;

long long sciezki(const vector<string>& plansza)
{
    if (plansza.empty() || plansza[0].empty())
        return 0;
    int wiersze = static_cast<int>(plansza.size());
    int kolumny = static_cast<int>(plansza[0].size());
    vector<vector<long long>> dp(wiersze, vector<long long>(kolumny, 0));
    dp[0][0] = plansza[0][0] == '#' ? 0 : 1;
    for (int i = 0; i < wiersze; ++i)
        for (int j = 0; j < kolumny; ++j)
        {
            if (plansza[i][j] == '#')
                continue;
            if (i > 0)
                dp[i][j] += dp[i - 1][j];
            if (j > 0)
                dp[i][j] += dp[i][j - 1];
        }
    return dp.back().back();
}

int main()
{
    cout << sciezki({"...", ".#.", "..."}) << '\n';
    cout << sciezki({"#..", "...", "..."}) << '\n';
    cout << sciezki({"...", "###", "..."}) << '\n';
    return 0;
}
