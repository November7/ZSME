#include <iostream>

using namespace std;

// przekazywanie argumentów do funkcji

void inc1(int a) // argument przekazywany przez wartość (tworzona jest kopia argumentu)
{
    cout << "wartosc argument w funkcji przed inkrementacja "<< a << endl; //123
    a++;
    cout << "wartosc argument w funkcji po inkrementacja "<< a << endl; //124
 
} //zmienna a jest usuwana z pamięci

void inc2(int& a) // argument przekazywany przez zmienną/przez referencję/przez alias (nie jest tworzona kopia argumentu, funkcja pracuje na oryginalnej zmiennej)
{
    cout << "wartosc argument w funkcji przed inkrementacja "<< a << endl; //123
    a++;
    cout << "wartosc argument w funkcji po inkrementacja "<< a << endl; //124
 
} //alias jest usuwany

#include <math.h>

void pierwiastki_r_kw(float a, float b, float c)
{
    if(a == 0)
    {
        cout<< "Rownanie nie jest kwadratowe: "<<endl; 
        return;
    }
    cout<< "Pierwiastki rownania kwadratowego: "; // y = ax^2 + bx + c
    float delta = b * b - 4 * a * c;
    if(delta < 0)
    {
        cout << "brak rozwiazan rzeczywistych" <<endl;
    }
    else if (delta == 0)
    {
        cout << -b/(2*a) <<endl;
    }
    else
    {
        cout<< (-b - sqrt(delta)) / (2 * a) <<", "<< (-b + sqrt(delta)) / (2 * a) << endl;
    }
}

int main()
{
    float a,b,c;
    cout<<"Podaj wspolczynniki rownania kwadratowego (ax^2 + bx + c): ";
    cin >> a >> b >> c;
    pierwiastki_r_kw(a,b,c);

    return 0;
}