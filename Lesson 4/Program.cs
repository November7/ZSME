/************************************************/
/*   Formatowanie danych w Console.Write(Line)  */
/************************************************/


class App
{
    static int valInt = -123456;
    static double valDouble = -123456.789012;
    enum Color {Yellow = 1, Blue, Green};
    static DateTime thisDate = DateTime.Now;

    public static void Main()
    {
        // Formatowanie typów liczbowych.
        //https://learn.microsoft.com/pl-pl/dotnet/standard/base-types/standard-numeric-format-strings
        Console.WriteLine("specyfikatory konwersji numeryczne");
        Console.WriteLine(
            "(C) Waluta: . . . . . . . . . . {0:C}\t{1:C}\n" +
            "(D) Dziesiętnie:. . . . . . . . {0:D}\n" +
            "(E) Notacja naukowa:  . . . . . {0:E}\t{1:E}\n" +
            "(F) Fixed point:. . . . . . . . {0:F}\t{1:F}\n" +  // np. {1:F4} - 4 cyfry po separatorze dziesiętnym
            "(G) Standardowy (domyśłny): . . {0:G}\t\t{1:G}\n" +
            "(0) Liczba: . . . . . . . . . . {0:00000.00000}\t{1:00000.00000}\n" +
            "(N) Liczba: . . . . . . . . . . {0:N8}\t{1:N8}\n" +
            "(P) Procent:. . . . . . . . . . {0:P}\t{1:P}\n" +
            "(R) Round-trip: . . . . . . . . {0:R}\t{1:R}\n" + //formatowanie bezstratne dla double/float
            "(b) Binarnie: . . . . . . . . . {0:B}\n" +
            "(x) Szesnastkowo: . . . . . . . {0:x}\n" +
            "(X) Szesnastkowo: . . . . . . . {0:X}\n",
            valInt, valDouble);

        // Formatowanie daty i czasu.
        Console.WriteLine("Specyfikatory konwersji daty i czasu:");
        Console.WriteLine(
            "(t) Czas krótki:. . . . . . . . {0:t}\n" +
            "(T) Czas długi: . . . . . . . . {0:T}\n" +
            "(d) Data krótka:. . . . . . . . {0:d}\n" +
            "(D) Data długa: . . . . . . . . {0:D}\n" +            
            "(M) Dzień, miesiąc: . . . . . . {0:M}\n" +
            "(Y) Miesiąc, rok: . . . . . . . {0:Y}\n" +            
            "(R) RFC1123:. . . . . . . . . . {0:R}\n" +
            "(s) Sortable: . . . . . . . . . {0:s}\n" +
            "(u) Universal sortable: . . . . {0:u} (invariant)\n" +
            "(U) Universal full date/time: . {0:U}\n" +
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
            "(DDDD) Miesiąc: . . . . . . . . {0:dddd}\n" +
            "(DDD) Miesiąc:. . . . . . . . . {0:ddd}\n" +
            "(HH) Godzina: . . . . . . . . . {0:HH}\n" +
            // "(HH) Godzina: . . . . . . . . . {0:HHH}\n" +
            // "(DD) Miesiąc: . . . . . . . . . {0:h}\n" +
            // "(DD) Miesiąc: . . . . . . . . . {0:mm}\n" +
            // "(DD) Miesiąc: . . . . . . . . . {0:m}\n" +
            "",
            thisDate);    

        // Formatowanie typu wyliczeniowego.
        Console.WriteLine("Specyfikatory typów wyliczeniowych");
        Console.WriteLine(
            "(G) Standardowy (domyślny): . . {0:G}\n" +
            "(F) Flagi:. . . . . . . . . . . {0:F} (flags or integer)\n" +
            "(D) Liczba dziesiętna:. . . . . {0:D}\n" +
            "(X) Szesnastkowo: . . . . . . . {0:X}\n",
            Color.Green);




            // c = -123;
// Console.WriteLine("{0:0000000000}",c);
// Console.WriteLine("{0:b}",c);
// Console.WriteLine("{0:x}",c);
// Console.WriteLine("{0:X}",c);
// Console.WriteLine("{0:n}",c);
// Console.WriteLine("{0:C2}",c);
// Console.WriteLine(c.ToString( "C2", CultureInfo.CreateSpecificCulture("en-US")));
// Console.WriteLine(c.ToString( "n", CultureInfo.CreateSpecificCulture("pl-PL")));
// Console.WriteLine(c.ToString( "n0",CultureInfo.InvariantCulture));
// // Ustawienia regionalne PL

// Console.WriteLine(String.Format(CultureInfo.InvariantCulture,"{0:0.000}", d));

// decimal dec = 123.10000000000000001m;
// Console.WriteLine(dec);

// double flo = 123.10000000000001; //ale już nie double flo = 123.000000000000001;
// Console.WriteLine($"{flo}");
    }
}
