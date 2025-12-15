// Liczby pierwsze 

#include <iostream>
using namespace std;

class punkt
{
public:
    punkt()
    {
        cout<<"Tworze nowy obiekt"<<endl;
        x = 0;
        y = 0;
    }

    int x; //4
    int y; //4
};



int main()
{
    punkt A,B,C;
    A.x = 123;
    A.y = 321;

    cout << A.x << " "<<A.y<<endl;
    cout << B.x << " "<<B.y<<endl;
    cout << C.x << " "<<C.y<<endl;
}
