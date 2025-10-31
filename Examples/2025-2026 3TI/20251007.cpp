#include <iostream>

using namespace std;



int main()
{
    // for
    cout<<"for"<<endl;
    for(int i = 0 ; i<10 ; ++i)
    {
        cout<<i<<endl;
    }
    
    // while
    cout<<"while"<<endl;    
    int i = 0;
    while(i<10)
    {
        cout<<i<<endl;
        ++i;
        //
    }
    
    //do..while
    cout<<"do..while"<<endl;    
    i = 0; 
    do
    {
        cout<<i<<endl;
        ++i;
    }
    while(i<10);

    return 0;
}