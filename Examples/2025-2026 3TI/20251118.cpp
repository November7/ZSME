#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
    
    srand(time(NULL));
    // cout<<RAND_MAX<<endl;

    for (int i = 0 ; i<10 ; i++) rand(); // <0, RAND_MAX)
  
    int dane[10];

    for (int i = 0 ; i<10 ; i++)
        dane[i] = int(100 * float(rand())/RAND_MAX); //<0, 100)

    for (int i = 0 ; i<10 ; i++)
        cout << dane[i] <<", ";

    // min i max

    int max = dane[0];
    for (int i = 1 ; i<10 ; i++)
    {
        if(dane[i] > max)
        {
            max = dane[i];
        }
    }
    cout<<endl<<"Najwieksza wartosc to: "<<max <<endl;


}