#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int plecak(const vector<int>& wagi, const vector<int>& wartosci, int pojemnosc)
{
    vector<int> dp(pojemnosc + 1, 0);
    for (size_t i = 0; i < wagi.size(); ++i)
        for (int w = pojemnosc; w >= wagi[i]; --w)
            dp[w] = max(dp[w], dp[w - wagi[i]] + wartosci[i]);
    return dp[pojemnosc];
}

int main()
{
    cout << plecak({2, 3, 4, 5}, {3, 4, 5, 6}, 5) << '\n';
    cout << plecak({2}, {3}, 4) << '\n';
    return 0;
}
