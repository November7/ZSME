#include <iostream>
#include <cstdint>
using namespace std;

struct RGB { unsigned char r, g, b; };
union Pixel
{
    uint16_t p16b;
    uint32_t p32b;
    RGB p24b;
};

int main()
{
    Pixel a{};
    a.p32b = 4321;
    cout << a.p32b << '\n';
    a.p16b = 1234;
    cout << a.p16b << '\n'; // czytamy tylko aktywny skladnik
    a.p24b = RGB{255, 128, 0};
    cout << +a.p24b.r << ' ' << +a.p24b.g << ' ' << +a.p24b.b << '\n';
    cout << "Rozmiar unii: " << sizeof(Pixel) << '\n';
    // Nie odczytujemy p32b po zapisaniu p24b jako sposobu konwersji koloru.
    // uint16_t i uint32_t wymagaja platformy udostepniajacej te typy.
}
