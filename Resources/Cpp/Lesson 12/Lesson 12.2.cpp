#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> liczby{1, 2, 3};
    for (auto it = liczby.begin(); it != liczby.end(); ++it)
        *it *= 2;
    for (auto it = liczby.rbegin(); it != liczby.rend(); ++it)
        cout << *it << ' ';
    cout << '\n';
    return 0;
}
