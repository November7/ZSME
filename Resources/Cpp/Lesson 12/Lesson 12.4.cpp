#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> liczby{1, 4, 2, 5, 3};
    int prog = 3;
    cout << count_if(liczby.begin(), liczby.end(),
        [prog](int liczba) { return liczba >= prog; }) << '\n';
    sort(liczby.begin(), liczby.end(),
        [](int a, int b) { return a > b; });
    for (int liczba : liczby)
        cout << liczba << ' ';
    cout << '\n';
    return 0;
}
