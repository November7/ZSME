#include <iostream>
#include <memory>
#include <utility>

using namespace std;

int main()
{
    auto liczba = make_unique<int>(42);
    auto nowyWlasciciel = move(liczba);
    cout << boolalpha << (liczba == nullptr) << '\n';
    cout << *nowyWlasciciel << '\n';
    auto wspolna = make_shared<int>(10);
    auto kopia = wspolna;
    *kopia = 20;
    cout << *wspolna << ' ' << wspolna.use_count() << '\n';
    return 0;
}
