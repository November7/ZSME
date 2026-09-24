#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> monety{1, 3, 4};
    int kwota = 6;
    vector<int> dp(kwota + 1, kwota + 1);
    vector<int> ostatniaMoneta(kwota + 1, -1);
    dp[0] = 0;
    for (int suma = 1; suma <= kwota; ++suma)
        for (int moneta : monety)
            if (moneta <= suma && dp[suma - moneta] + 1 < dp[suma])
            {
                dp[suma] = dp[suma - moneta] + 1;
                ostatniaMoneta[suma] = moneta;
            }
    if (dp[kwota] > kwota)
    {
        cout << -1 << '\n';
        return 0;
    }
    cout << dp[kwota] << '\n';
    for (int suma = kwota; suma > 0; suma -= ostatniaMoneta[suma])
        cout << ostatniaMoneta[suma] << ' ';
    cout << '\n';
    return 0;
}
