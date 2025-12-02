// Liczby pierwsze 

#include <iostream>

using namespace std;

int main()
{   
    int i = 2;
    while(i < 1000)
    {
        bool flag = true;
        for(int j = 2; j*j <= i ; j++)
        {
            if (i % j == 0)
            {
                flag = false;
                break;
            } 
        }
        if (flag)
        {
            cout << i <<", ";
        }        
        i++;
    }


    return 0;   
}