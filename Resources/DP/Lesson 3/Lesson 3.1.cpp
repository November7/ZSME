#include <iostream>
#include <vector>

using namespace std;

long long fibonacci(int n, vector<long long>& memo)
{
    if (memo[n] != -1)
        return memo[n];
    if (n < 2)
        return memo[n] = n;
    return memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
}

int main()
{
    int n = 40;
    vector<long long> memo(n + 1, -1);
    cout << fibonacci(n, memo) << '\n';
    return 0;
}
