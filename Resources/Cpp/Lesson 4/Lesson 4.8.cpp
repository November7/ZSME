#include <iostream>
using namespace std;

int main()
{
    int a = 3;
    int b = 6;
    int c = 9;

    int* tabWsk[3] = {&a, &b, &c};

    for (int i = 0; i < 3; i++)
    {
        cout << *tabWsk[i] << endl;
    }

    return 0;
}