#include <iostream>
#include <string>

using namespace std;

template <typename T, typename U = int>
struct Para
{
    T pierwszy;
    U drugi;
};

int main()
{
    Para<string> wynik{"Ala", 5};
    Para<int, double> pomiar{1, 2.5};
    cout << wynik.pierwszy << ' ' << wynik.drugi << '\n';
    cout << pomiar.pierwszy << ' ' << pomiar.drugi << '\n';
    return 0;
}
