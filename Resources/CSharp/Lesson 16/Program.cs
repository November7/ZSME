static void PrintItems<T>(IEnumerable<T> items)
{
    foreach (T item in items)
    {
        Console.WriteLine(item);
    }
}

List<int> numbers = [7, 2, 9, 2, 5];
Console.WriteLine("Elementy listy:");
PrintItems(numbers);

HashSet<int> uniqueNumbers = [.. numbers];
Console.WriteLine($"Liczba różnych wartości: {uniqueNumbers.Count}");

Dictionary<string, int> grades = new()
{
    ["Ala"] = 5,
    ["Jan"] = 4,
    ["Ola"] = 6
};

Console.WriteLine("Oceny posortowane według ucznia:");
foreach (KeyValuePair<string, int> entry in grades.OrderBy(entry => entry.Key))
{
    Console.WriteLine($"{entry.Key}: {entry.Value}");
}