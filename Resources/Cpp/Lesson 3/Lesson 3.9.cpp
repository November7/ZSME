#include <iostream>
using namespace std;

void PrzezWartosc(int arg) { ++arg; }
void PrzezReferencje(int& arg) { ++arg; }

int main()
{
    int x = 5;
    PrzezWartosc(x);
    cout << "Po przekazaniu przez wartosc: " << x << '\n'; // 5
    PrzezReferencje(x);
    cout << "Po przekazaniu przez referencje: " << x << '\n'; // 6
}
