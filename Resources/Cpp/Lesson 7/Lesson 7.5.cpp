#include <iostream>
using namespace std;

class Wektor2D
{
public:
    int x;
    int y;

    Wektor2D(int px, int py)
    {
        x = px;
        y = py;
    }

    Wektor2D operator+(const Wektor2D& drugi)
    {
        return Wektor2D(x + drugi.x, y + drugi.y);
    }
};

int main()
{
    Wektor2D a(2, 5);
    Wektor2D b(3, 4);
    Wektor2D c = a + b;

    cout << c.x << " " << c.y << endl;

    return 0;
}