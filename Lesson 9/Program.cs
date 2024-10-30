class App
{
    static void Main()
    {
        // Random random1 = new();
        // Console.WriteLine(random1.Next());
        // #pragma warning disable IDE0090
        // Random random1b = new Random();
        // var random1c = new Random();

        // Console.WriteLine(random2.Next());

        Random random = new();

        // Lista

        Console.WriteLine("Lista");
        List<int> Lista1 = new();
        // List<int> Lista1b = new List<int>();

        for (int i = 0; i < 10; i++)
        {
            Lista1.Add(random.Next(10));
        }
        
        foreach (var item in Lista1)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        for (int i = 0; i < Lista1.Count; i++)
        {
            Console.Write($"{Lista1[i]}, ");
        }
        Console.WriteLine();

        Lista1.RemoveAt(5);        
        Console.WriteLine(string.Join(", ", Lista1));
        Lista1.Insert(0,123);
        Console.WriteLine(string.Join(", ", Lista1));

        // List<object> Lista2 = new List<object>();
        List<object> Lista2 = new();
        Lista2.Add(1);
        Lista2.Add(2.5);
        Lista2.Add("tekst");
        Lista2.Add(true);

        foreach (var item in Lista2)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        List<object> Lista3 = [1,2,3,"randomowy tekst",3.123,2,4,5,5];

        // foreach (var item in Lista3)
        // {
        //     Console.Write($"{item}, ");
        // }
        // Console.WriteLine();

        // //Klasa Tuple
        // Console.WriteLine("Klasa Tuple");
        // Tuple<int, string> Krotka1 = new Tuple<int, string>(1, "tekst");
        // Tuple<int, string, float> Krotka2 = new (1, "tekst", 3.5f);

        // Console.WriteLine($"{Krotka1.Item1}, {Krotka1.Item2}");
        // Console.WriteLine($"{Krotka2.Item1}, {Krotka2.Item2}, {Krotka2.Item3}");
        // Console.WriteLine($"{Krotka1.GetType()}\n{Krotka2.GetType()}\n");

        // // Krotka1.Item1 = 123; //błąd - elementy tylko do odczytu

        // //Krotka wartości (Value Tuple)
        // Console.WriteLine("Value Tuple");
        
        // (int, float, string) WarKrotka1 = (1, 3.14f, "tekst");
        // Console.WriteLine($"{WarKrotka1.Item1}, {WarKrotka1.Item2}, {WarKrotka1.Item3}");

        // var WarKrotka2 = (1, 2, 3, 4);
        // Console.WriteLine($"{WarKrotka2.Item1}, {WarKrotka2.Item2}, {WarKrotka2.Item3}");

        // WarKrotka1.Item1 = 123;
        // WarKrotka2.Item2 = 321;
       
        // var WarKrotka3 = (a:1, b:3.14f, c:"tekst");
        // Console.WriteLine($"{WarKrotka3.a}, {WarKrotka3.b}, {WarKrotka3.c}");
        // WarKrotka3.a = 123;

        // (int a, float b, string c) WarKrotka4 = (1, 3.14f, "tekst");
        // Console.WriteLine($"{WarKrotka4.a}, {WarKrotka4.b}, {WarKrotka4.c}");
       
        // Console.WriteLine($"{WarKrotka1.GetType()}\n{WarKrotka2.GetType()}\n{WarKrotka3.GetType()}\n{WarKrotka4.GetType()}");


        //Zbiór
        // #pragma warning disable IDE0028
        HashSet<int> Zbior1a = new HashSet<int> {7, 2, 3, 4, 5};
        HashSet<int> Zbior1b = new () {7, 2, 3, 4, 5};
        HashSet<int> Zbior1c =  [7, 2, 3, 4, 5];

        Zbior1a.Add(5);
        Zbior1a.Add(5);
        Zbior1a.Add(6);
        Zbior1a.Remove(3);

        foreach (var item in Zbior1a)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        HashSet<string> Zbior2 = ["ala","ma","kota","a","sierotka","ma","Rysia"];
        // Console.WriteLine($"{Zbior1a},{Zbior2}");

        foreach (var item in Zbior2)
        {
            Console.Write($"{item}, ");
        }
        Console.WriteLine();

        //Słownik
        // #pragma warning disable IDE0090
        Dictionary<string, int> dict1 = new Dictionary<string, int>
        {
            { "Alice", 30 },
            { "Bob", 25 },
            { "Charlie", 35 }
        };

        // Dictionary<string, int> dict2 = new() { { "Alice", 30 }, { "Bob", 25 }};

        // Dodawanie elementów do słownika
        dict1.Add("David", 40);
        // dict2.Add("David", 40);

        // Wyświetlanie zawartości słownika
        foreach (var item in dict1) //KeyValuePair
        {
            Console.WriteLine($"Key: {item.Key}, Value: {item.Value}");
        }

        // Uzyskiwanie wartości na podstawie klucza
        if (dict1.TryGetValue("Alice", out int age))
        {
            Console.WriteLine($"Age of Alice: {age}");
        }
    
    }

}
