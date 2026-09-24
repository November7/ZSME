#include <iostream>
#include <vector>

using namespace std;

int bruteForce(int n)
{
    int wynik = 0;
    for (unsigned maska = 0; maska < (1U << n); ++maska)
    {
        int suma = 0;
        bool poprawna = true;
        for (int i = 0; i < n; ++i)
        {
            if (suma >= n)
            {
                if ((maska >> i) != 0)
                    poprawna = false;
                break;
            }
            suma += (maska & (1U << i)) ? 2 : 1;
        }
        if (poprawna && suma == n)
            ++wynik;
    }
    return wynik;
}

int rekurencja(int n)
{
    if (n < 0)
        return 0;
    if (n == 0)
        return 1;
    return rekurencja(n - 1) + rekurencja(n - 2);
}

int tabulacja(int n)
{
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; ++i)
    {
        dp[i] = dp[i - 1];
        if (i >= 2)
            dp[i] += dp[i - 2];
    }
    return dp[n];
}

int main()
{
    int n = 5;
    cout << bruteForce(n) << ' ' << rekurencja(n) << ' ' << tabulacja(n) << '\n';
    return 0;
}
