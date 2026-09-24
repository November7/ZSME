#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> koszt{2, 5, 1, 3, 2};
    int n = static_cast<int>(koszt.size());
    vector<int> dp(n, 0);
    dp[n - 1] = koszt[n - 1];
    dp[n - 2] = koszt[n - 2] + dp[n - 1];
    for (int i = n - 3; i >= 0; --i)
        dp[i] = koszt[i] + min(dp[i + 1], dp[i + 2]);
    cout << dp[0] << '\n';
    return 0;
}
