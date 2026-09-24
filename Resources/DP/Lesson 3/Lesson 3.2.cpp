#include <iostream>
#include <vector>

using namespace std;

long long fibonacci(int n, vector<long long>& memo, vector<bool>& obliczone)
{
    if (obliczone[n])
        return memo[n];
    if (n < 2)
        memo[n] = n;
    else
        memo[n] = fibonacci(n - 1, memo, obliczone) + fibonacci(n - 2, memo, obliczone);
    obliczone[n] = true;
    return memo[n];
}

int main()
{
    int n = 10;
    vector<long long> memo(n + 1, 0);
    vector<bool> obliczone(n + 1, false);
    cout << fibonacci(n, memo, obliczone) << '\n';
    cout << memo[0] << ' ' << boolalpha << obliczone[0] << '\n';
    return 0;
}
