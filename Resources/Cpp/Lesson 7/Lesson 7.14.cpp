#include <iostream>
using namespace std;
class CExample
{
    int m_attr = 7;
public:
    static int m_count;
    static void showCount() { cout << m_count << '\n'; }
    static void showObject(const CExample& obiekt)
    {
        cout << obiekt.m_attr << '\n'; // konkretny obiekt udostepniono argumentem
    }
};
int CExample::m_count = 0; // definicja poza klasa
int main()
{
    CExample::showCount(); // obiekt nie jest potrzebny
    CExample obj;
    obj.showCount(); // dozwolone, lecz zapis przez nazwe klasy jest czytelniejszy
    CExample::m_count = 3;
    cout << obj.m_count << '\n'; // to samo wspolne pole
    CExample::showObject(obj);
}
