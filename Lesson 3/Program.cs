using System.Globalization;
using System.Net.NetworkInformation;

/************************************************/
/*                Typy danych                   */
/************************************************/

//Definicja typu znakowego:


System.Char c = 'c'; 
char c1 = 'a'; //char to alias od System.Char
Console.WriteLine($"{c}, {c1}");

//char c2 = 123; // błąd niejawnej konwersji int -> char
// niejawna konwersja jest możliwa tylko z typu mniejszego do typu większego (gdy nie ma ryzyka utraty części danych). 
// W pozostałych przypadkach konieczna jest jawna konwersja lub parsowanie
char c2 = (char)123; // prawidłowa 'jawna' konwersja z int -> char
//char c3 = char(123); // nieprawudłowa jawna konwesja w notacji funkcyjnej...
Console.WriteLine(c2);

byte b1 = 255; //System.Byte
sbyte b2 = -128;

Console.WriteLine($"{b1} {b2}");

//Min max typu danych
Console.WriteLine($"Min: {byte.MinValue}, Max: {byte.MaxValue}");

int i1 = 2_147_483_647; //System.Int
Console.WriteLine($"{i1}  <{int.MinValue}, {int.MaxValue}>");

// uint i2 = 4_294_967_295;
// short i4 = 32767;
// ushort i5 = 65535;
// long i3 = 9_223_372_036_854_775_807;
// ulong i6 = 18_446_744_073_709_551_615;

bool b = true; // true/false
Console.WriteLine($"{b}");

float f1 = 3.14f; // lub 3.14F
double f2 = 3.14; // lub 3.14g lub 3.14G
decimal f3 = 3.14m; // lub 3.14M

Console.WriteLine($"{f1} {f2} {f3}");

// string s = "";


// Console.WriteLine("{0} {1} {2} {3} {4} {5} {6}, {7}",a,b,c,c1,c2,d,e,s);

// // Formatowanie liczb: https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings

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


int? zmienna = null;

Console.WriteLine($"Wartość zmiennej: {zmienna}");


int[] T = [1,2,3];

foreach(int i in T)
    Console.WriteLine(i);


string[] vowels = ["a", "e", "i", "o", "u"];
string[] consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                       "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"];
string[] alphabet = [.. vowels, .. consonants, "y"];

foreach(string s in alphabet)
    Console.WriteLine(s);