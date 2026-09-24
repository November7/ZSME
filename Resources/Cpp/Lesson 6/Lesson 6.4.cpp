#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long Licznik;
using Wektor = vector<int>;

int main()
{
    Licznik liczba = 10000000000ULL;
    Wektor wyniki{10, 20, 30};
    cout << liczba << ' ' << wyniki.size() << '\n';
    return 0;
}
