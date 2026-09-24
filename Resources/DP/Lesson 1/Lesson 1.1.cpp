#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> monety{1, 3, 4};
    int kwota = 6;
    vector<int> dp(kwota + 1, kwota + 1);
    dp[0] = 0;
    for (int suma = 1; suma <= kwota; ++suma)
        for (int moneta : monety)
            if (moneta <= suma)
                dp[suma] = min(dp[suma], dp[suma - moneta] + 1);
    cout << dp[kwota] << '\n';
    return 0;
}
