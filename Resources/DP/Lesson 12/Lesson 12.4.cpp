#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int waga = 2, wartosc = 3, pojemnosc = 4;
    vector<int> jednokrotnie(pojemnosc + 1, 0);
    vector<int> wielokrotnie(pojemnosc + 1, 0);
    for (int w = pojemnosc; w >= waga; --w)
        jednokrotnie[w] = max(jednokrotnie[w], jednokrotnie[w - waga] + wartosc);
    for (int w = waga; w <= pojemnosc; ++w)
        wielokrotnie[w] = max(wielokrotnie[w], wielokrotnie[w - waga] + wartosc);
    cout << "0/1: " << jednokrotnie[pojemnosc] << '\n';
    cout << "Bez ograniczen: " << wielokrotnie[pojemnosc] << '\n';
    return 0;
}
