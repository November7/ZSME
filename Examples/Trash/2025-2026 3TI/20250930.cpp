#include <iostream>

using namespace std;

int main() 
{
    // int a, b, c;
    // cout << "Podaj a, b, c" << endl;

    // cin >> a >> b >> c;
    
    // for(int i = a ; i < b ; i += c)
    // {
    //     cout<<i<<endl;        
    // }
    
    int n = 10;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << i * j<<"\t";
        }
        cout<<endl;
    }
    
    return 0;
}