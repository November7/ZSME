#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> unikalne{3, 1, 2, 2};
    multiset<int> wszystkie{3, 1, 2, 2};
    unikalne.insert(4);
    cout << unikalne.count(2) << ' ' << wszystkie.count(2) << '\n';
    for (int liczba : unikalne)
        cout << liczba << ' ';
    cout << '\n';
    return 0;
}
