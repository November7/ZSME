#include <iostream>

using namespace std;

struct Punkt
{
    double x;
    double y;
};

int main()
{
    Punkt punkt{2.0, 3.0};
    punkt.x += 1.0;
    cout << punkt.x << ' ' << punkt.y << '\n';
    return 0;
}
