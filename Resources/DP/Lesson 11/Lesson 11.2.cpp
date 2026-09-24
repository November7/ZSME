#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int lcs(const string& a, const string& b)
{
    int n = static_cast<int>(a.size()), m = static_cast<int>(b.size());
    vector<int> poprzedni(m + 1, 0), obecny(m + 1, 0);
    for (int i = 1; i <= n; ++i)
    {
        obecny[0] = 0;
        for (int j = 1; j <= m; ++j)
            if (a[i - 1] == b[j - 1])
                obecny[j] = poprzedni[j - 1] + 1;
            else
                obecny[j] = max(poprzedni[j], obecny[j - 1]);
        swap(poprzedni, obecny);
    }
    return poprzedni[m];
}

int main()
{
    cout << lcs("ABCBDAB", "BDCABA") << '\n';
    cout << lcs("", "ABC") << '\n';
    return 0;
}
