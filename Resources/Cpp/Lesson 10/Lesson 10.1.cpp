#include <iostream>

using namespace std;

template <typename T>
T wieksza(T a, T b)
{
    return a > b ? a : b;
}

int main()
{
    cout << wieksza(3, 7) << '\n';
    cout << wieksza(2.5, 1.5) << '\n';
    cout << wieksza<double>(3, 4.5) << '\n';
    return 0;
}
