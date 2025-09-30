#include <iostream>

using namespace std;

int main()
{
    int x, y;
    cout << "Podaj dwie liczby" <<endl;
    cin >> x >> y;

    cout << "Suma: " << x + y << endl;
    cout << "Roznica: " << x - y << endl;
    cout << "Iloczyn: " << x * y << endl;
    if(y == 0) 
    {
        cout<<"Nie dziel przez zero!"<<endl;
    }
    else
    {
        cout << "Iloraz: " << float(x) / float(y) << endl;
    }
    return 0;
}