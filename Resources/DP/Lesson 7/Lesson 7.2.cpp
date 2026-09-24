#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> koszt{2, 5, 1, 3, 2};
    int n = static_cast<int>(koszt.size());
    vector<int> dp(n), poprzedni(n, -1);
    dp[0] = koszt[0];
    for (int i = 1; i < n; ++i)
    {
        poprzedni[i] = i - 1;
        if (i >= 2 && dp[i - 2] < dp[i - 1])
            poprzedni[i] = i - 2;
        dp[i] = koszt[i] + dp[poprzedni[i]];
    }
    vector<int> sciezka;
    for (int i = n - 1; i != -1; i = poprzedni[i])
        sciezka.push_back(i);
    reverse(sciezka.begin(), sciezka.end());
    cout << dp.back() << '\n';
    for (int i : sciezka)
        cout << i << ' ';
    cout << '\n';
    return 0;
}
