#include <iostream>
using namespace std;


int main()
{
    int i, j;
    int R = 15;

    for(i=0 ; i < R; i++) //y 
    {
        for(j=0 ; j < R; j++) //x
        {
            //L
            // if(j == 0  ||  i == R-1) cout << "*" ;
            // else cout << " ";
            
            //C
            // if(j == 0  || i == R-1 || i == 0) cout << "*" ;
            // else cout << " ";

            //E
            // if(j == 0  || i == R-1 || i == 0 || i == R/2) cout << "*" ;
            // else cout << " ";

            //N Z X
             if(i == -j + R-1 || i == j) cout << "*" ;
            else cout << " ";

        }
        cout<<endl;
    }

    return 0;
}


