#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int cel = 7;
    vector<int> skoki{1, 3, 5};
    vector<long long> dp(cel + 1, 0);
    dp[0] = 1;
    for (int i = 0; i <= cel; ++i)
        for (int skok : skoki)
            if (i + skok <= cel)
                dp[i + skok] += dp[i];
    cout << dp[cel] << '\n';
    return 0;
}
