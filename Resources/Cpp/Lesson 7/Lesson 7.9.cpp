#include <iostream>
using namespace std;
class CExample
{
    int x, y;
public:
    CExample() : x(0), y(0) {}
    CExample(int a, int b) : x(a), y(b) {}
    CExample(const CExample& org) : x(org.x), y(org.y) {}
    void Print() const { cout << x << ' ' << y << '\n'; }
};
int main()
{
    CExample a;
    CExample b(3, 4);
    CExample c(b);
    a.Print(); b.Print(); c.Print();
}
