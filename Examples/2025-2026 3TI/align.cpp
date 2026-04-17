#include <iostream>

using namespace std;

using serialNumber = char[30];
using barCode = int;
using text = char[50];

#pragma pack(push, 4)
union ID
{
    serialNumber sn;
    barCode bc;
};

struct Product
{
    ID id;
    text name;
    float price;
    bool isBC;
};

#pragma pack(pop)

int main()
{
    cout << "Rozmiar "<<sizeof(Product) << endl;
}