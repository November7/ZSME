#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
    vector<int> liczby{4, 1, 3, 2, 3};
    sort(liczby.begin(), liczby.end());
    cout << boolalpha << binary_search(liczby.begin(), liczby.end(), 3) << '\n';
    auto pozycja = lower_bound(liczby.begin(), liczby.end(), 3);
    cout << distance(liczby.begin(), pozycja) << '\n';
    for (int liczba : liczby)
        cout << liczba << ' ';
    cout << '\n';
    return 0;
}
