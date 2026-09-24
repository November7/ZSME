#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> plansza{"...", ".#.", "..."};
    int n = static_cast<int>(plansza.size());
    vector<long long> dp(n, 0);
    dp[0] = 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (plansza[i][j] == '#')
                dp[j] = 0;
            else if (j > 0)
                dp[j] += dp[j - 1];
    cout << dp.back() << '\n';
    return 0;
}
