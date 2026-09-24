#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

int main()
{
    map<string, int> oceny{{"Ala", 5}, {"Ola", 4}};
    oceny["Jan"] = 3;
    for (const auto& [imie, ocena] : oceny)
        cout << imie << ' ' << ocena << '\n';
    unordered_map<string, int> zliczenia;
    for (const string& slowo : vector<string>{"kot", "pies", "kot"})
        ++zliczenia[slowo];
    auto znalezione = zliczenia.find("kot");
    if (znalezione != zliczenia.end())
        cout << znalezione->first << ' ' << znalezione->second << '\n';
    return 0;
}
