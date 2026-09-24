#include <iostream>
#include <memory>
#include <stdexcept>
#include <exception>

using namespace std;

class Zasob
{
public:
    Zasob()
    {
        cout << "Utworzono zasob\n";
    }

    ~Zasob()
    {
        cout << "Zwolniono zasob\n";
    }
};

int main()
{
    try
    {
        auto zasob = make_unique<Zasob>();
        throw runtime_error("Przerwano operacje");
    }
    catch (const exception& blad)
    {
        cout << blad.what() << '\n';
    }
    return 0;
}
