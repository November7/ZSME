#include <iostream>
#include <vector>
#include <initializer_list>

using namespace std;

int main()
{
    int n = 6;
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int stopien = 1; stopien <= n; ++stopien)
        for (int skok : {1, 2})
            if (stopien >= skok)
                dp[stopien] += dp[stopien - skok];
    for (int stopien = 0; stopien <= n; ++stopien)
        cout << stopien << ' ' << dp[stopien] << '\n';
    return 0;
}
