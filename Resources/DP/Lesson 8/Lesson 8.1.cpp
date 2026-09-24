#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int wiersze = 3, kolumny = 4;
    vector<vector<long long>> dp(wiersze, vector<long long>(kolumny, 0));
    dp[0][0] = 1;
    for (int i = 0; i < wiersze; ++i)
        for (int j = 0; j < kolumny; ++j)
        {
            if (i > 0)
                dp[i][j] += dp[i - 1][j];
            if (j > 0)
                dp[i][j] += dp[i][j - 1];
        }
    for (const auto& wiersz : dp)
    {
        for (long long liczba : wiersz)
            cout << liczba << ' ';
        cout << '\n';
    }
    cout << dp.back().back() << '\n';
    return 0;
}
