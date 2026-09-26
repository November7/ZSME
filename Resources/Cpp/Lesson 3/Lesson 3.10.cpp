#include <iostream>
using namespace std;

void funkcja(int arg) { cout << "Wartosc: " << arg << '\n'; }
void funkcja(int& arg) { cout << "Referencja: " << arg << '\n'; }

int main()
{
    int x = 5;
    funkcja(5); // int& nie moze zwiazac sie z tymczasowa wartoscia 5
    // funkcja(x); // blad kompilacji: obie wersje pasuja

    // Jawny wybor konkretnej wersji przez typ wskaznika do funkcji:
    void (*przezWartosc)(int) = funkcja;
    void (*przezReferencje)(int&) = funkcja;
    przezWartosc(x);
    przezReferencje(x);
}
