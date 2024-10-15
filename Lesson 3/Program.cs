/************************************************/
/*                Typy danych                   */
/************************************************/

// class App
// {
//     static void Main()
//     {
//         //Definicja typu znakowego:
//         System.Char c1 = 'c'; 
//         char c2 = 'a'; //char to alias od System.Char
//         Console.WriteLine($"{c1}, {c2}");
//         // Console.WriteLine("{0}, {1}",c1,c2);

//         // char c2 = 123; // błąd niejawnej konwersji int -> char
//         // niejawna konwersja jest możliwa tylko z typu mniejszego do typu większego 
//         //(gdy nie ma ryzyka utraty części danych). 
//         // W pozostałych przypadkach konieczna jest jawna konwersja lub parsowanie

//         char c3 = (char)123; // prawidłowa 'jawna' konwersja z int -> char
//         //char c3 = char(123); // nieprawidłowa jawna konwesja w notacji funkcyjnej...
//         Console.WriteLine(c3);

//         byte b1 = 255; //System.Byte
//         sbyte b2 = -128; //127

//         Console.WriteLine($"{b1} {b2}");

//         //Min max typu danych
//         Console.WriteLine($"Min: {byte.MinValue}, Max: {byte.MaxValue}");

//         int i1 = 2_147_483_647; //System.Int
//         Console.WriteLine($"{i1} Min: <{int.MinValue}, Max: {int.MaxValue}>");

//         // uint i2 = 4_294_967_295;
//         // short i4 = 32767;
//         // ushort i5 = 65535;
//         // long i3 = 9_223_372_036_854_775_807;
//         // ulong i6 = 18_446_744_073_709_551_615;

//         bool b = true; // true/false
//         Console.WriteLine($"{b}");

//         float f1 = 3.14f; // lub 3.14F
//         double f2 = 3.14; // lub 3.14g lub 3.14G
//         decimal f3 = 3.14m; // lub 3.14M

//         Console.WriteLine($"{f1} {f2} {f3}");
//         Console.WriteLine($"float: ({float.MinValue}, {float.MaxValue})");
//         Console.WriteLine($"double: ({double.MinValue}, {double.MaxValue})");
//         Console.WriteLine($"decimal: ({decimal.MinValue}, {decimal.MaxValue})");
//     }
// }


/************************************************/
/*                Konwersja typów               */
/************************************************/

// class App
// {
//     static void Main()
//     {
//         Console.Write("Wprowadź liczbę: ");
//         string? inp = Console.ReadLine();

//         int nLiczba;
//         // nLiczba = int.Parse(inp); // Uwaga na wyjątki!!!
//         // Console.WriteLine($"Liczba: {nLiczba}");

//         bool ok = int.TryParse(inp, out nLiczba);
//         if (ok)
//         {
//             Console.WriteLine($"Liczba: {nLiczba}");
//         }

//         double dLiczba = nLiczba; // Konwersja prosta (niejawna)
//         Console.WriteLine($"Liczba (double): {dLiczba}");

//         dLiczba = (double) nLiczba; // Konwersja jawna
//         Console.WriteLine($"Liczba (double): {dLiczba}");

//         dLiczba = 3.14;
//         // nLiczba = dLiczba; // Konwersja niedozwolona
//         nLiczba = (int) dLiczba; // Konwersja wymagana
//         Console.WriteLine($"Liczba: {nLiczba}");
//     }
// }



/************************************************/
/*                Zasięg zmiennych              */
/************************************************/
class App
{
    static void Main()
    {
        int i = 3;
        
        // for(int i=0;i<10;i++) //błąd zmienna i już została zdefiniowana w zewnętrznym zakresie
        // {                   
        //     Console.WriteLine(i);
        // }
        
        for(i=0;i<10;i++)
        {                
            Console.WriteLine(i);
        }


        // Console.WriteLine(i); 
    }
}