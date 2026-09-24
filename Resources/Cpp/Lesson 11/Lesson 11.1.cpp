#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> liczby{10, 20, 30};
    liczby.push_back(40);
    liczby.at(1) = 25;
    liczby.erase(liczby.begin());
    liczby.pop_back();
    for (int liczba : liczby)
        cout << liczba << ' ';
    cout << '\n' << liczby.size() << '\n';
    return 0;
}
