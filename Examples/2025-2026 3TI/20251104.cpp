#include <iostream>

#define MAX 1000

using namespace std;

int main()
{
    int n;
    cout << "Podaj ilosc danych" << endl;
    cin >> n;

    if (n < 1 || n > MAX)
    {
        cout <<"Nieprawidlowe dane wejsciow!"<<endl;
        return 1;
    }

    int dane[MAX];

    for(int i = 0; i < n ; i++)
    {
        cout<<"Podaj wartosc #"<<(i+1)<<": ";
        cin>>dane[i];
    }
    cout<<endl;

    for(int i = 0; i < n ; i++)
    {        
        cout<<dane[i]<<", ";
    }
    cout<<endl;
    
    // suma i średnia elementów
    int suma = 0;
    for(int i = 0; i < n ; i++)
    {        
        suma += dane[i];
        // suma = suma + dane[i];
    }
    cout << "Suma elementow tablicy wynosi: " << suma << endl;
    cout << "Srednia elementow tablicy wynosi: " << float(suma) / n << endl;


    // znajdź wartość min i max:

    return 0;
}