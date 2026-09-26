#include <iostream>
using namespace std;
class CExample
{
    int m_attr = 0;
    static int m_count;
public:
    CExample() { ++m_count; }
    explicit CExample(int a) : m_attr(a) { ++m_count; }
    CExample(const CExample& org) : m_attr(org.m_attr) { ++m_count; }
    CExample& operator=(const CExample&) = default; // nie powstaje nowy obiekt
    ~CExample() { --m_count; }
    static void showCount() { cout << "Liczba obiektow: " << m_count << '\n'; }
};
int CExample::m_count = 0;
void SomeFunction(CExample arg)
{
    (void)arg;
    CExample::showCount(); // dodatkowa kopia parametru
}
int main()
{
    CExample::showCount(); // 0
    {
        CExample a, b(10);
        CExample::showCount(); // 2
        SomeFunction(a); // 3 wewnatrz funkcji
        SomeFunction(b); // 3 wewnatrz funkcji
        CExample::showCount(); // 2
    }
    CExample::showCount(); // 0
}
