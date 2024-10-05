/************************************************/
/*                Typy danych                   */
/************************************************/
class App
{
    static void Main()
    {
        //Definicja typu znakowego:
        System.Char c1 = 'c'; 
        char c2 = 'a'; //char to alias od System.Char
        Console.WriteLine($"{c1}, {c2}");

        //char c2 = 123; // błąd niejawnej konwersji int -> char
        // niejawna konwersja jest możliwa tylko z typu mniejszego do typu większego (gdy nie ma ryzyka utraty części danych). 
        // W pozostałych przypadkach konieczna jest jawna konwersja lub parsowanie

        char c3 = (char)123; // prawidłowa 'jawna' konwersja z int -> char
        //char c3 = char(123); // nieprawidłowa jawna konwesja w notacji funkcyjnej...
        Console.WriteLine(c3);

        byte b1 = 255; //System.Byte
        sbyte b2 = -128;

        Console.WriteLine($"{b1} {b2}");

        //Min max typu danych
        Console.WriteLine($"Min: {byte.MinValue}, Max: {byte.MaxValue}");

        int i1 = 2_147_483_647; //System.Int
        Console.WriteLine($"{i1} Min: <{int.MinValue}, Max: {int.MaxValue}>");

        // uint i2 = 4_294_967_295;
        // short i4 = 32767;
        // ushort i5 = 65535;
        // long i3 = 9_223_372_036_854_775_807;\
        // ulong i6 = 18_446_744_073_709_551_615;

        bool b = true; // true/false
        Console.WriteLine($"{b}");

        float f1 = 3.14f; // lub 3.14F
        double f2 = 3.14; // lub 3.14g lub 3.14G
        decimal f3 = 3.14m; // lub 3.14M

        Console.WriteLine($"{f1} {f2} {f3}");

        // string s = "";


        // Console.WriteLine("{0} {1} {2} {3} {4} {5} {6}, {7}",a,b,c,c1,c2,d,e,s);
    }
}

/************************************************/
/*                Zasięg zmiennych              */
/************************************************/
// class App
// {
//     static void Main()
//     {
//         // int x = 3;

//         {
//             int x;
//             x = 3;
//             Console.WriteLine(x);
//         }

//         // Console.WriteLine(x);
//     }
// }