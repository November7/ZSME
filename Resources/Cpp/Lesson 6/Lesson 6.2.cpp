#include <iostream>
using namespace std;

struct Flagi
{
    unsigned int aktywny : 1;
    unsigned int administrator : 1;
    unsigned int premium : 1;
};

int main()
{
    Flagi f = {1, 0, 1};

    cout << "aktywny: " << f.aktywny << endl;
    cout << "administrator: " << f.administrator << endl;
    cout << "premium: " << f.premium << endl;

    return 0;
}