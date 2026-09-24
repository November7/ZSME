#include <iostream>
#include <stack>
#include <queue>
#include <initializer_list>

using namespace std;

int main()
{
    stack<int> stos;
    queue<int> kolejka;
    priority_queue<int> priorytety;
    for (int liczba : {3, 1, 2})
    {
        stos.push(liczba);
        kolejka.push(liczba);
        priorytety.push(liczba);
    }
    while (!stos.empty())
    {
        cout << stos.top() << ' ' << kolejka.front() << ' ' << priorytety.top() << '\n';
        stos.pop();
        kolejka.pop();
        priorytety.pop();
    }
    return 0;
}
