#include <iostream>
using namespace std;

float Suma(float a, float b)
{
    return a + b;
}
float Roznica(float a, float b)
{
    return a - b;
}
float Iloczyn(float a, float b)
{
   return a * b;
}
float Iloraz(float a, float b)
{
    if (b == 0) 
    {
        cout<<"Nie dziel przez zero!";
        return 0;
    }
    else return a / b;
}

unsigned long int Silnia(int n)
{
    long int w = 1;
    for(int i = 1 ; i <= n ; i++)
    {
        w *= i;
    }
    return w;
}

int main()
{
    float x, y;
    cout << "Podaj argumenty dzialania: ";
    cin >> x >> y;
    cout<<"Wynik dodawania "<<x<<" i "<<y<<" wynosi: "<<Suma(x,y)<<endl;
    cout<<"Wynik odejmowania "<<x<<" i "<<y<<" wynosi: "<<Roznica(x,y)<<endl;
    cout<<"Wynik mnozenia "<<x<<" i "<<y<<" wynosi: "<<Iloczyn(x,y)<<endl;
    if(y != 0) cout<<"Wynik dzielenia "<<x<<" i "<<y<<" wynosi: "<<Iloraz(x,y)<<endl;
    cout<<"Wynik silni z "<<x<<" wynosi: "<<Silnia(x)<<endl;

    return 0;
}