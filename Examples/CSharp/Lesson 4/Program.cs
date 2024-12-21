/************************************************/
/*   Formatowanie danych w Console.Write(Line)  */
/************************************************/
using System.Globalization;

class App
{
    static int valInt = -123456;
    static double valDouble = -123456.789012;
    static int ujemna = -1, dodatnia = 1, zero = 0;
    enum Color {Yellow = 1, Blue, Green};
    static DateTime thisDate = DateTime.Now;

    public static void Main()
    {
        // Formatowanie typów liczbowych.
        //https://learn.microsoft.com/pl-pl/dotnet/standard/base-types/standard-numeric-format-strings

        Console.WriteLine("Standardowe specyfikatory konwersji numeryczne");
        Console.WriteLine(
            "(C) Waluta: . . . . . . . . . . {0:C}\t{1:C}\n" +
            "(D) Dziesiętnie:. . . . . . . . {0:D}\n" +
            "(E) Notacja naukowa:  . . . . . {0:E}\t{1:E}\n" +
            "(F) Fixed point:. . . . . . . . {0:F}\t{1:F}\n" +  // np. {1:F4} - 4 cyfry po separatorze dziesiętnym
            "(G) Standardowy (domyśłny): . . {0:G}\t\t{1:G}\n" +
            "(N) Liczba: . . . . . . . . . . {0:N8}\t{1:N8}\n" +
            "(P) Procent:. . . . . . . . . . {0:P}\t{1:P}\n" +
            "(R) Round-trip: . . . . . . . . {0:R}\t{1:R}\n" + //formatowanie bezstratne dla double/float
            "(b) Binarnie: . . . . . . . . . {0:B}\n" +
            "(x) Szesnastkowo: . . . . . . . {0:x}\n" +
            "(X) Szesnastkowo: . . . . . . . {0:X}\n",
            valInt, valDouble);


        Console.WriteLine("Niestandardowe specyfikatory konwersji numeryczne");
        Console.WriteLine(
            
            "(0) Liczba: . . . . . . . . . . {0:00000000.00000000}\t{1:00000000.00000000}\n" +
            "(#) Liczba: . . . . . . . . . . {0:########.########}\t\t\t{1:########.########}\n"+
            "(E) Liczba: . . . . . . . . . . {0:########.########E+000}\t\t\t{1:########.########E+000}\n"+
            "(%) Liczba: . . . . . . . . . . {0:########.########%}\t\t\t{1:########.########%}\n"+ 
            "(,) Liczba: . . . . . . . . . . {0:########,########}\t\t\t{1:#,#.#######}\n"+
            "(,,) Liczba:. . . . . . . . . . {0:########,########,}\t\t\t{1:########,########,}\n"+            
            "(;) Liczba: . . . . . . . . . . {2:Ujemne: #;Dodatnie: #;OMG ZERO} {3:Ujemne: #;Dodatnie: #;OMG ZERO} {4:Ujemne: #;Dodatnie: #;OMG ZERO}\n",
            valInt, valDouble,
            ujemna, zero, dodatnia);
        // \\ i @ \

        // Formatowanie daty i czasu.
        Console.WriteLine("Standardowe Specyfikatory konwersji daty i czasu:");
        Console.WriteLine(
            "(t) Czas krótki:. . . . . . . . {0:t}\n" +
            "(T) Czas długi: . . . . . . . . {0:T}\n" +
            "(d) Data krótka:. . . . . . . . {0:d}\n" +
            "(D) Data długa: . . . . . . . . {0:D}\n" +            
            "(M) Dzień, miesiąc: . . . . . . {0:M}\n" +
            "(Y) Miesiąc, rok: . . . . . . . {0:Y}\n" +            
            "(R) RFC1123:. . . . . . . . . . {0:R}\n" +
            "(s) Sortowalna: . . . . . . . . {0:s}\n" +
            "(u) UTC sortowalny: . . . . . . {0:u}\n" +
            "(U) UTC Pełna data/czas:. . . . {0:U}\n" +
            "(f) Pełna data/czas krótki: . . {0:f}\n" +
            "(F) Pełna data/czas długi:. . . {0:F}\n" +
            "(g) Domyślny data/czas krótki:. {0:g}\n" +
            "(G) Domyślny data/czas długi: . {0:G}\n",
            thisDate);


            Console.WriteLine("Specyfikatory konwersji składników daty i czasu:");
            Console.WriteLine(
            "(YYYY) Rok: . . . . . . . . . . {0:yyyy}\n" +
            "(YY) Rok: . . . . . . . . . . . {0:yy}\n" +
            "(MMMM) Miesiąc: . . . . . . . . {0:MMMM}\n" +
            "(MMM) Miesiąc:  . . . . . . . . {0:MMM}\n" +
            "(MM) Miesiąc: . . . . . . . . . {0:MM}\n" +
            "(dddd) Dzień: . . . . . . . . . {0:dddd}\n" +
            "(ddd) Dzień:. . . . . . . . . . {0:ddd}\n" +
            "(dd) Dzień: . . . . . . . . . . {0:dd}\n" +
            "(HH) Godzina: . . . . . . . . . {0:HH}\n" +
            "(hh) Godzina: . . . . . . . . . {0:hh}\n" +
            "(mm) Minuta: . . . . . . . . . {0:mm}\n" +
            "(ss) Sekundy: . . . . . . . . . {0:ss}\n" +
            "(ff) 0.01 Sekundy: . . . . . . . {0:ff}\n" +
            "(fff) 0.001 Sekundy: . . . . . . {0:fff}\n" +
            "(ffff) 0.0001 Sekundy: . . . . . {0:ffff}\n",
            thisDate);    

        // Formatowanie typu wyliczeniowego.
        Console.WriteLine("Specyfikatory typów wyliczeniowych");
        Console.WriteLine(
            "(G) Standardowy (domyślny): . . {0:G}\n" +
            "(F) Flagi:. . . . . . . . . . . {0:F}\n" +
            "(D) Liczba dziesiętna:. . . . . {0:D}\n" +
            "(X) Szesnastkowo: . . . . . . . {0:X}\n",
            Color.Green);


        //Nadpisanie ustawień regionalnych

        double c = 3.14;            
        Console.WriteLine(c.ToString( "C2", CultureInfo.CreateSpecificCulture("en-US")));
        Console.WriteLine(c.ToString( "C2", CultureInfo.CreateSpecificCulture("pl-PL")));
        Console.WriteLine(c.ToString( "N2", CultureInfo.InvariantCulture));
        
    }
}
