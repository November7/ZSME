#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minimalnyKoszt(const vector<int>& koszt)
{
    if (koszt.empty())
        return 0;
    vector<int> dp(koszt.size(), 0);
    dp[0] = koszt[0];
    if (koszt.size() > 1)
        dp[1] = dp[0] + koszt[1];
    for (size_t i = 2; i < koszt.size(); ++i)
        dp[i] = koszt[i] + min(dp[i - 1], dp[i - 2]);
    return dp.back();
}

int main()
{
    cout << minimalnyKoszt({2, 5, 1, 3, 2}) << '\n';
    cout << minimalnyKoszt({}) << '\n';
    cout << minimalnyKoszt({7}) << '\n';
    return 0;
}
