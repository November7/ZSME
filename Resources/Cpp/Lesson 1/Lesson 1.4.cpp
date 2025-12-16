#include <iostream>
using namespace std;

int main()
{
    int day;
    cout << "Podaj liczbę od 1 do 7 jako dzień tygodnia: ";
    cin >> day;
    switch (day) 
    {
        case 1:
            cout << "Poniedzialek" << endl;
            break;
            // brak instrukcji break; spowoduje "przechodzenie" do kolejnych przypadków
            // aż do napotkania break lub koniec switch
        case 2:
            cout << "Wtorek" << endl;
            break;
        case 3:
            cout << "Sroda" << endl;
            break;
        case 4:
            cout << "Czwartek" << endl;
            break;
        case 5:
            cout << "Piatek" << endl;   
            break;
        case 6:
            cout << "Sobota" << endl;
            break;
        case 7:
            cout << "Niedziela" << endl;
            break;
        default:
            cout << "Nieprawidłowa liczba dnia tygodnia!" << endl;
        
    }
    return 0;
}