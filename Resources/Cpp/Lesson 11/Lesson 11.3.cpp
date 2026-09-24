#include <iostream>
#include <list>
#include <iterator>

using namespace std;

int main()
{
    list<int> liczby{3, 1, 2, 2};
    liczby.push_front(5);
    liczby.push_back(4);
    auto pozycja = next(liczby.begin());
    liczby.insert(pozycja, 6);
    liczby.erase(pozycja);
    liczby.sort();
    liczby.unique();
    for (int liczba : liczby)
        cout << liczba << ' ';
    cout << '\n';
    return 0;
}
