#include <iostream>
using namespace std;

int main()
{
    int liczby[4] = {10, 20, 30, 40};
    int* wsk = &liczby[2];

    cout << "Element: " << *wsk << endl;
    cout << "Poprzedni: " << *(wsk - 1) << endl;
    cout << "Nastepny: " << *(wsk + 1) << endl;

    return 0;
}