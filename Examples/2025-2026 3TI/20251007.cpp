#include <iostream>

using namespace std;



int main()
{
    // for
    cout<<"Petla for"<<endl;
    for(int i=0 ; i<10 ; ++i)
    {
        cout<<i<<endl;  
    }
    
    // while
    
    int i = 0;
    cout<<"Petla while"<<endl;
    while(i<10)
    {
        cout<< i <<endl;        
        ++i;
    }
    
    i = 0;
    cout<<"Petla do..while"<<endl;
    do
    {
        cout<<i++<<endl;        
        // i++;
    } 
    while(i<10);

 

    return 0;
}