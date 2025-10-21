#include <iostream>
using namespace std;


int main()
{
    int i, j;
    int R = 11;

    for(i=0 ; i < R; i++)
    {
        for(j=0 ; j < R; j++)
        {
            // if(i == 0 || j == R/2) cout << "*" ; //T
            // else cout << " ";

            // if(i == R - 1 || j == 0) cout << "*" ; //L
            // else cout << " ";

            // if(i == R - 1 || j == 0 || j == R-1) cout << "*" ; //U
            // else cout << " ";
            
            // if(i == R - 1 || j == 0 || i == R/2 || i == 0) cout << "*" ; //E
            // else cout << " ";
            //N
            //Z
            //X
            if(i == j || j == -i + R-1) cout << "*" ; 
            else cout << " ";

        }
        cout<<endl;
    }

    return 0;
}


