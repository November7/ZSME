#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

int minimumMonet(const vector<int>& monety, int kwota)
{
    if (kwota < 0)
        throw invalid_argument("Kwota musi byc nieujemna");
    for (int moneta : monety)
        if (moneta <= 0)
            throw invalid_argument("Nominal musi byc dodatni");
    vector<int> dp(kwota + 1, -1);
    dp[0] = 0;
    for (int suma = 1; suma <= kwota; ++suma)
        for (int moneta : monety)
            if (moneta <= suma && dp[suma - moneta] != -1)
            {
                int kandydat = dp[suma - moneta] + 1;
                if (dp[suma] == -1 || kandydat < dp[suma])
                    dp[suma] = kandydat;
            }
    return dp[kwota];
}

int main()
{
    cout << minimumMonet({}, 0) << '\n';
    cout << minimumMonet({}, 3) << '\n';
    cout << minimumMonet({2}, 3) << '\n';
    cout << minimumMonet({2}, 4) << '\n';
    try
    {
        cout << minimumMonet({0, 2}, 4) << '\n';
    }
    catch (const invalid_argument& blad)
    {
        cout << blad.what() << '\n';
    }
    return 0;
}
