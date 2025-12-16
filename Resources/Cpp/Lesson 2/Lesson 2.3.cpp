#include <iostream>
using namespace std;

int main()
{
    int i = 0;
    do
    {
        cout << "Iteracja numer: " << i + 1 << endl;
        i++;
    } while (i < 5);
    // warunek jest sprawdzany po każdej iteracji pętli
    // więc pętla wykona się przynajmniej raz
    
    return 0;
}