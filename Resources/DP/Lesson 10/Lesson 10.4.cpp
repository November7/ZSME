#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int main()
{
    vector<int> wymiary{10, 30, 5, 60};
    int n = static_cast<int>(wymiary.size()) - 1;
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int dlugosc = 2; dlugosc <= n; ++dlugosc)
        for (int lewy = 0; lewy + dlugosc <= n; ++lewy)
        {
            int prawy = lewy + dlugosc - 1;
            dp[lewy][prawy] = numeric_limits<long long>::max();
            for (int podzial = lewy; podzial < prawy; ++podzial)
            {
                long long koszt = dp[lewy][podzial] + dp[podzial + 1][prawy]
                    + 1LL * wymiary[lewy] * wymiary[podzial + 1] * wymiary[prawy + 1];
                dp[lewy][prawy] = min(dp[lewy][prawy], koszt);
            }
        }
    cout << dp[0][n - 1] << '\n';
    return 0;
}
