#include <iostream>
#include <string>

using namespace std;

int main()
{
    string tekst = "Ala ma kota";
    tekst += ".";
    cout << tekst.substr(0, 3) << '\n';
    auto pozycja = tekst.find("kota");
    if (pozycja != string::npos)
        tekst.replace(pozycja, 4, "psa");
    cout << tekst << '\n';
    return 0;
}
