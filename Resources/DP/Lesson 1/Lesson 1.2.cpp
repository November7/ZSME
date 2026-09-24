#include <iostream>
#include <vector>

using namespace std;

long long fibonacci(int n, vector<int>& wywolania)
{
    ++wywolania[n];
    if (n < 2)
        return n;
    return fibonacci(n - 1, wywolania) + fibonacci(n - 2, wywolania);
}

int main()
{
    int n = 6;
    vector<int> wywolania(n + 1, 0);
    cout << fibonacci(n, wywolania) << '\n';
    for (int i = 0; i <= n; ++i)
        cout << i << ' ' << wywolania[i] << '\n';
    return 0;
}
