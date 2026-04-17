#include <iostream>

using namespace std;

struct Punkt2D
{
    float x, y; // 4 + 4 = 8 B        
};

union Test
{
    int x; //4B
    short y; //2B
};

int main()
{
    /********
      
     char - 1B
     2B = short [int] <= int <= long [int] = 4B = 32b
     float - 4B
     double - 8B
     long double - 16B
     long long int - 8B
     */

     Test A;
     cout << sizeof(A) << endl;
     A.x = 123;
     A.y = 'a';
     cout << A.x << " " <<A.y<<endl;



    return 0;
}