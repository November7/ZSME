#include <iostream>
#include <vector>

using namespace std;

bool sumaPodzbioru(const vector<int>& liczby, int cel)
{
    vector<bool> dp(cel + 1, false);
    dp[0] = true;
    for (int liczba : liczby)
        for (int suma = cel; suma >= liczba; --suma)
            dp[suma] = dp[suma] || dp[suma - liczba];
    return dp[cel];
}

int main()
{
    cout << boolalpha << sumaPodzbioru({3, 5, 7}, 10) << '\n';
    cout << sumaPodzbioru({3, 5, 7}, 6) << '\n';
    cout << sumaPodzbioru({}, 0) << '\n';
    return 0;
}
