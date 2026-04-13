#include <iostream>
using namespace std;

class Punkt
{
public:
    int x;
    int y;

    void pokaz()
    {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

int main()
{
    Punkt p;
    p.x = 3;
    p.y = 7;
    p.pokaz();

    return 0;
}