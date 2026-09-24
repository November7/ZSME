#include <iostream>

using namespace std;

int main()
{
    int rozmiar = 5;
    int* liczby = new int[rozmiar]{};
    for (int i = 0; i < rozmiar; ++i)
    {
        liczby[i] = i * i;
        cout << liczby[i] << ' ';
    }
    cout << '\n';
    delete[] liczby;
    return 0;
}
