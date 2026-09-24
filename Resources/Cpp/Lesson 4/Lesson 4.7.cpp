#include <iostream>

using namespace std;

int main()
{
    int liczby[3] = {10, 20, 30};
    int (*wskaznik)[3] = &liczby;
    for (int i = 0; i < 3; ++i)
        cout << (*wskaznik)[i] << '\n';
    return 0;
}
