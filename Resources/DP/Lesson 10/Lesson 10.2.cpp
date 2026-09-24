#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lis(const vector<int>& liczby)
{
    int n = static_cast<int>(liczby.size());
    vector<int> dp(n, 1);
    int wynik = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i; ++j)
            if (liczby[j] < liczby[i])
                dp[i] = max(dp[i], dp[j] + 1);
        wynik = max(wynik, dp[i]);
    }
    return wynik;
}

int main()
{
    cout << lis({10, 9, 2, 5, 3, 7, 101, 18}) << '\n';
    cout << lis({2, 2, 2}) << '\n';
    cout << lis({}) << '\n';
    return 0;
}
