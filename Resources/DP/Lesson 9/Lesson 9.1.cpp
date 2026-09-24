#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int plecak(int i, int miejsce, const vector<int>& wagi, const vector<int>& wartosci)
{
    if (i == static_cast<int>(wagi.size()))
        return 0;
    int wynik = plecak(i + 1, miejsce, wagi, wartosci);
    if (wagi[i] <= miejsce)
        wynik = max(wynik, wartosci[i] + plecak(i + 1, miejsce - wagi[i], wagi, wartosci));
    return wynik;
}

int main()
{
    vector<int> wagi{2, 3, 4, 5};
    vector<int> wartosci{3, 4, 5, 6};
    cout << plecak(0, 5, wagi, wartosci) << '\n';
    return 0;
}
