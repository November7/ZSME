#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    vector<int> liczby{1, 2, 3, 4, 5};
    liczby.erase(remove_if(liczby.begin(), liczby.end(),
        [](int x) { return x % 2 == 0; }), liczby.end());
    transform(liczby.begin(), liczby.end(), liczby.begin(),
        [](int x) { return x * x; });
    cout << accumulate(liczby.begin(), liczby.end(), 0) << '\n';
    return 0;
}
