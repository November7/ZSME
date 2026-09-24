#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> monety{1, 2};
    int kwota = 3;
    vector<long long> kombinacje(kwota + 1, 0), uporzadkowane(kwota + 1, 0);
    kombinacje[0] = uporzadkowane[0] = 1;
    for (int moneta : monety)
        for (int suma = moneta; suma <= kwota; ++suma)
            kombinacje[suma] += kombinacje[suma - moneta];
    for (int suma = 1; suma <= kwota; ++suma)
        for (int moneta : monety)
            if (suma >= moneta)
                uporzadkowane[suma] += uporzadkowane[suma - moneta];
    cout << "Kombinacje: " << kombinacje[kwota] << '\n';
    cout << "Kolejnosc ma znaczenie: " << uporzadkowane[kwota] << '\n';
    return 0;
}
