#include <iostream>
using namespace std;

struct Student
{
    char imie[20];
    char nazwisko[20];
    int nr_systemowy;
};

int main()
{
    struct Student uczen1{}; // zapis poprawny w C i C++
    Student uczen2{"Jan", "Nowak", 123}; // C++ nie wymaga slowa struct
    Student* p = &uczen2;
    uczen1.nr_systemowy = 333;
    cout << uczen1.nr_systemowy << '\n';
    cout << uczen2.imie << ' ' << uczen2.nazwisko << ' ' << uczen2.nr_systemowy << '\n';
    p->nr_systemowy = 444;
    cout << uczen2.nr_systemowy << '\n';
}
