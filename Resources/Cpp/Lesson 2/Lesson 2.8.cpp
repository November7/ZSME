#include <iostream>
using namespace std;

int main()
{
	int i = 0;
	int suma = 0;

	do
	{
		suma += i;
		i += 2;
	}
	while (i <= 100);

	cout << "Suma liczb parzystych od 0 do 100 wynosi: " << suma <<endl;
	return 0;
}
