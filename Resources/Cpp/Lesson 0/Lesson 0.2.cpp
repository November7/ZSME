#include <iostream>
using namespace std;
 
int main(int argc, char ** argv)
{
	cout << argc << endl;
	cout << argv[0] << endl;
	return 0;
}

// Wywołanie programu z linii poleceń może wyglądać następująco:
// ./nazwa_aplikacji arg1 arg2 arg3