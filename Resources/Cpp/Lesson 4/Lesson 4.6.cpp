#include <iostream>

using namespace std;

int main()
{
    int liczby[] = {10, 20, 30};
    int* wskaznik = &liczby[0];
    for (int i = 0; i < 3; ++i)
        cout << *(wskaznik + i) << '\n';
    return 0;
}
