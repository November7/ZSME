#include <iostream>

using namespace std;

class Wektor
{
public:
    int x;
    int y;

    Wektor operator+(const Wektor& drugi) const
    {
        return {x + drugi.x, y + drugi.y};
    }

    bool operator==(const Wektor& drugi) const
    {
        return x == drugi.x && y == drugi.y;
    }
};

int main()
{
    Wektor a{1, 2}, b{3, 4};
    Wektor suma = a + b;
    cout << suma.x << ' ' << suma.y << '\n';
    cout << boolalpha << (a == b) << '\n';
    return 0;
}
