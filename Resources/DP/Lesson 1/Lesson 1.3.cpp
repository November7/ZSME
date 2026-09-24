#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> koszt{2, 5, 1, 3, 2};
    vector<int> dp(koszt.size());
    dp[0] = koszt[0];
    dp[1] = dp[0] + koszt[1];
    for (size_t i = 2; i < koszt.size(); ++i)
        dp[i] = koszt[i] + min(dp[i - 1], dp[i - 2]);
    for (int wynik : dp)
        cout << wynik << ' ';
    cout << '\n';
    return 0;
}
