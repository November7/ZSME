#include <iostream>
using namespace std;

int main()
{
	int suma = 0;

	for(int i=0 ; i<10 ; i++)
	{
		suma += i;
	}

	cout << "Suma liczb od 0 do 9 wynosi: "<< suma <<endl;
	return 0;
}
