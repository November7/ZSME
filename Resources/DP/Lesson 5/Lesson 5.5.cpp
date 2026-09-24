#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> skoki{2, 4};
    int cel = 7;
    int nieosiagalny = cel + 1;
    vector<int> dp(cel + 1, nieosiagalny);
    dp[0] = 0;
    for (int i = 1; i <= cel; ++i)
        for (int skok : skoki)
            if (i >= skok && dp[i - skok] != nieosiagalny)
                dp[i] = min(dp[i], dp[i - skok] + 1);
    cout << (dp[cel] == nieosiagalny ? -1 : dp[cel]) << '\n';
    return 0;
}
