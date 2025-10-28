#include <iostream>

using namespace std;

int main() 
{
    // definicja tablicy 1

    int tab1[10]; //10 x 4B
    for(int i = 0; i<10 ; i++)
    {
        cout << tab1[i] << ", ";
    }
    cout<<endl;

    //definicja tablicy 2 z lista inicjalizacyjną
    int tab2[5] = {4, 5, 3, 2, 5};
    for(int i = 0; i<5 ; i++)
    {
        cout << tab2[i] << ", ";
    }
    cout<<endl;

    //definicja tablicy 3 z lista inicjalizacyjną
    int tab3[10] = {4, 5, 3, 2, 5};
    for(int i = 0; i<10 ; i++)
    {
        cout << tab3[i] << ", ";
    }
    cout<<endl;

    return 0;
}