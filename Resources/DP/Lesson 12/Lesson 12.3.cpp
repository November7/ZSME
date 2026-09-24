#include <iostream>
#include <vector>

using namespace std;

int sumaDzielIZwyciezaj(const vector<int>& liczby, int lewy, int prawy, int& wywolania)
{
    ++wywolania;
    if (lewy == prawy)
        return 0;
    if (prawy - lewy == 1)
        return liczby[lewy];
    int srodek = lewy + (prawy - lewy) / 2;
    int a = sumaDzielIZwyciezaj(liczby, lewy, srodek, wywolania);
    int b = sumaDzielIZwyciezaj(liczby, srodek, prawy, wywolania);
    return a + b;
}

int fibonacci(int n, vector<int>& memo, int& stany)
{
    if (memo[n] != -1)
        return memo[n];
    ++stany;
    if (n < 2)
        return memo[n] = n;
    int a = fibonacci(n - 1, memo, stany);
    int b = fibonacci(n - 2, memo, stany);
    return memo[n] = a + b;
}

int main()
{
    vector<int> liczby{1, 2, 3, 4, 5, 6, 7, 8};
    int wywolania = 0;
    int suma = sumaDzielIZwyciezaj(liczby, 0, static_cast<int>(liczby.size()), wywolania);
    cout << "Dziel i zwyciezaj: " << suma << ' ' << wywolania << '\n';
    vector<int> memo(9, -1);
    int stany = 0;
    int wynik = fibonacci(8, memo, stany);
    cout << "DP: " << wynik << ' ' << stany << '\n';
    return 0;
}
