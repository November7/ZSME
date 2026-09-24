#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int zachlannie(const vector<int>& malejaceMonety, int kwota)
{
    int wynik = 0;
    for (int moneta : malejaceMonety)
    {
        wynik += kwota / moneta;
        kwota %= moneta;
    }
    return kwota == 0 ? wynik : -1;
}

int dynamicznie(const vector<int>& monety, int kwota)
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
    vector<int> monety{4, 3, 1};
    cout << zachlannie(monety, 6) << '\n';
    cout << dynamicznie(monety, 6) << '\n';
    return 0;
}
