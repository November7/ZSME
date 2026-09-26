#include <iostream>
#include <initializer_list>
using namespace std;

int main()
{
    for (int wybor : {1, 2, 3, 4, 9})
    {
        cout << "Wybor: " << wybor << '\n';
        switch (wybor)
        {
            case 1:
            case 2:
            case 3:
                cout << "Wspolne instrukcje dla 1, 2 i 3\n";
                [[fallthrough]]; // celowe przejscie dalej, C++17
            case 4:
            default:
                cout << "Instrukcje koncowe\n";
                break;
        }
    }
}
