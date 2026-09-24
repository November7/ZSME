#include <iostream>

using namespace std;

int main()
{
    int a = 10, b = 20, c = 30;
    int* wskazniki[] = {&a, &b, &c};
    for (int* wskaznik : wskazniki)
        *wskaznik += 1;
    cout << a << ' ' << b << ' ' << c << '\n';
    return 0;
}
