// using System.Runtime.CompilerServices;

// class App
//  {
//     static void Main()
//     {
//         //Instrukcja warunkowa:

//         int nLiczba = 5;

//         if (nLiczba % 2 == 0)
//         {
//             Console.WriteLine("Liczba jest parzysta.");
//         }
//         else
//         {
//             Console.WriteLine("Liczba jest nieparzysta.");
//         }

//         //Instrukcja warunkowa z wykorzystaniem składni zagnieżdżonych:

        
//         if (nLiczba % 2 == 0)
//         {
//             Console.WriteLine("Liczba jest parzysta.");
//         }
//         else
//         {
//             if (nLiczba % 3 == 0)
//             {
//                 Console.WriteLine("Liczba jest podzielna przez 3.");
//             }
//             else
//             {
//                 Console.WriteLine("Liczba nie jest parzysta ani podzielna przez 3.");
//             }
//         }

//         if (nLiczba % 2 == 0)
//         {
//             Console.WriteLine("Liczba jest parzysta.");
//         }
//         else if (nLiczba % 3 == 0)
//         {
//             Console.WriteLine("Liczba jest podzielna przez 3.");
//         }
//         else
//         {
//             Console.WriteLine("Liczba nie jest parzysta ani podzielna przez 3.");
//         }

//         //Instrukcja warunkowa z wykorzystaniem operatora warunkowego (operator ternarny):

//         Console.WriteLine((nLiczba % 2 == 0 && nLiczba % 3 == 0) ? "Liczba jest parzysta i podzielna przez 3." : "Liczba nie jest parzysta ani podzielna przez 3.");        


//     }
// }
class App
 {
    static void Main()
    {
        int x = 123;
        switch (x)
        {
            case 1:
                Console.WriteLine("x = 1");
                break;
            case 2:
                Console.WriteLine("x = 2");
                break;
            case 3:
                Console.WriteLine("x = 3");
                break;
            default:
                Console.WriteLine("x nie jest 1, 2, lub 3");
                break;
        }


        string s = "123";

        switch (s)
        {
            default:
                Console.WriteLine("s nie jest 1, 2, lub 3");
                break;
            case "1":
                Console.WriteLine("s = 1");
                break;
            case "2":
                Console.WriteLine("s = 2");
                break;
            case "3":
                Console.WriteLine("s = 3");
                break;
        }
    }

}