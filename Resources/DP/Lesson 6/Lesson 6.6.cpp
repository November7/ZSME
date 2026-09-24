#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> monety{1, 2, 5};
    int kwota = 5;
    vector<long long> dp(kwota + 1, 0);
    dp[0] = 1;
    for (int moneta : monety)
        for (int suma = moneta; suma <= kwota; ++suma)
            dp[suma] += dp[suma - moneta];
    cout << dp[kwota] << '\n';
    return 0;
}
