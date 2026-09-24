#include <iostream>
#include <memory>

using namespace std;

class Figura
{
public:
    virtual double pole() const = 0;
    virtual ~Figura() = default;
};

class Kwadrat : public Figura
{
    double bok;

public:
    explicit Kwadrat(double a) : bok(a) {}

    double pole() const override
    {
        return bok * bok;
    }
};

int main()
{
    unique_ptr<Figura> figura = make_unique<Kwadrat>(4);
    cout << figura->pole() << '\n';
    return 0;
}
