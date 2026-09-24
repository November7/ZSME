#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> skoki{1, 3, 5};
    int cel = 7;
    vector<long long> dp(cel + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= cel; ++i)
        for (int skok : skoki)
            if (i >= skok)
                dp[i] += dp[i - skok];
    cout << dp[cel] << '\n';
    return 0;
}
