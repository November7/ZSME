#include <iostream>

using namespace std;

struct Uprawnienia
{
    unsigned odczyt : 1;
    unsigned zapis : 1;
    unsigned wykonanie : 1;
};

int main()
{
    Uprawnienia prawa{1, 0, 1};
    prawa.zapis = 1;
    cout << prawa.odczyt << ' ' << prawa.zapis << ' ' << prawa.wykonanie << '\n';
    return 0;
}
