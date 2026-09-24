#include <iostream>
#include <array>
#include <deque>

using namespace std;

int main()
{
    array<int, 3> stale{1, 2, 3};
    deque<int> kolejka(stale.begin(), stale.end());
    kolejka.push_front(0);
    kolejka.push_back(4);
    kolejka.pop_front();
    for (int liczba : kolejka)
        cout << liczba << ' ';
    cout << '\n';
    return 0;
}
