#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minimumMonet(const vector<int>& monety, int kwota)
{
    vector<int> dp(kwota + 1, kwota + 1);
    dp[0] = 0;
    for (int suma = 1; suma <= kwota; ++suma)
        for (int moneta : monety)
            if (moneta <= suma)
                dp[suma] = min(dp[suma], dp[suma - moneta] + 1);
    return dp[kwota] > kwota ? -1 : dp[kwota];
}

int main()
{
    cout << minimumMonet({1, 3, 4}, 6) << '\n';
    cout << minimumMonet({2, 4}, 7) << '\n';
    cout << minimumMonet({2, 4}, 0) << '\n';
    return 0;
}
