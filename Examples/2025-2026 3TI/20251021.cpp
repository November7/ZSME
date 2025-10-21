#include <iostream>
using namespace std;

int main()
{

    int n = 0;
    cout << "Podaj liczbę!" << endl;
    cin >> n;
    int i = 0;

    //1 napisz program który wypisuje na ekran n liczb o 0 do n-1 za pomocą pętli for
    
    for(i = 0 ; i < n ; i++)
    {
        cout << i << ", ";
    }
    cout<<endl;
    
   
    //2 napisz program który wypisuje na ekran n liczb o 0 do n-1 za pomocą pętli while
    i = 0;
    while( i < n )
    {
        cout << i << ", ";
        i++;
    }
    cout<<endl;
    
    //3 napisz program który wypisuje na ekran n liczb o 0 do n-1 za pomocą pętli do .. while
    i = 0;
    do
    {
        cout << i << ", ";
        i++;
    }
    while( i < n);
    cout<<endl; 

    return 0;
}


