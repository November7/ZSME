#include <iostream>
using namespace std;

//deklaracja funkcji (która nic nie zwraca i nie przyjmuje parametrów)
void funkcja(); 

int main()
{
    //wywołanie (użycie) funkcji
    funkcja();    
    return 0;
}

//definicja funkcji
void funkcja()
{
    cout << "To jest przykladowa funkcja." << endl;
}