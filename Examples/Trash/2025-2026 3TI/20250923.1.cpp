#include <iostream>

using namespace std;

int main() 
{
    int a, b;

    cout << "Podaj dwie liczby"<<endl;
    cin >> a >> b;

    cout << "Suma: "<<a + b<<endl;
    cout << "Roznica: "<<a - b<<endl;
    cout << "Iloczyn: "<<a * b<<endl;
    if( b == 0)
    {
        //  
        cout << "Nie mozna dzielic przez zero!"<<endl;  
    }
    else
    {
        cout << "Iloraz: "<< float(a) / float(b)<<endl;
    }


    return 0;
}