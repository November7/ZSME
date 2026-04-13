#include <iostream>
using namespace std;

int main()
{
    int liczby[3] = {7, 14, 21};
    int (*wskTab)[3] = &liczby;

    cout << (*wskTab)[0] << endl;
    cout << (*wskTab)[1] << endl;
    cout << (*wskTab)[2] << endl;

    return 0;
}