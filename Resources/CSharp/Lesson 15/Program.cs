class App
{
    static void Main()
    {
        string path = Path.Combine(Path.GetTempPath(), "lekcja-csharp.txt");

        try
        {
            File.WriteAllText(path, "Pierwszy wiersz\nDrugi wiersz");
            File.AppendAllText(path, "\nDopisany wiersz");

            foreach (string line in File.ReadAllLines(path))
            {
                Console.WriteLine(line);
            }

            string input = "123";
            int number = int.Parse(input);
            Console.WriteLine($"Odczytana liczba: {number}");
        }
        catch (FormatException exception)
        {
            Console.WriteLine($"Niepoprawny format liczby: {exception.Message}");
        }
        catch (IOException exception)
        {
            Console.WriteLine($"Błąd operacji na pliku: {exception.Message}");
        }
        finally
        {
            if (File.Exists(path))
            {
                File.Delete(path);
            }
        }
    }
}