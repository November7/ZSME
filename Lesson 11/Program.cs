class KlasaBazowa
{
    public KlasaBazowa()
    {
        Console.WriteLine("Konstruktor klasy bazowej");
    }

    public void PrzykladowaMetoda()
    {
        Console.WriteLine("Jakaś metoda z klasy bazowej");
    }
}


static class KlasaRozszerzajacaInneKlasy
{
    
    public static void NowaMetoda(this KlasaBazowa obj) 
    { 
        Console.WriteLine("New method"); 
    } 

    public static string Capitalize(this string obj)
    {
        return obj[0].ToString().ToUpper() + obj.Substring(1).ToLower();
    }

    public static string Title(this string obj, string sep = " ")
    {
        string[] parts = obj.Split(sep);
        for(int i = 0 ; i<parts.Length; i++)
        {
            parts[i] = parts[i].Capitalize();
        }

        return string.Join(sep,parts);
    }
}

class Program 
{ 
    static void Main() 
    { 
        KlasaBazowa obj = new (); 
        obj.PrzykladowaMetoda(); 
        obj.NowaMetoda(); 


        string test = "ala ma kota";
        Console.WriteLine(test.Capitalize());
        Console.WriteLine(test.Title());
    } 
}