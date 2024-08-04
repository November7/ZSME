using System.Globalization;
using System.Net.NetworkInformation;

/************************************************/
/*                Typy danych                   */
/************************************************/

char a = 'a';
// char a1 = 123;
byte a2 = 255;
sbyte a3 = 127;
bool b = true;
int c = 2_147_483_647; 
short c1 = 32767;
long c2 = 9_223_372_036_854_775_807;
ushort c3 = 65535;
uint c4 = 4_294_967_295;
ulong c5 = 18_446_744_073_709_551_615;

float d = 3.14f;
double e = 3.14;
string s = "";


Console.WriteLine("{0} {1} {2} {3} {4} {5} {6}, {7}",a,b,c,c1,c2,d,e,s);

// Formatowanie liczb: https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings

c = -123;
Console.WriteLine("{0:0000000000}",c);
Console.WriteLine("{0:b}",c);
Console.WriteLine("{0:x}",c);
Console.WriteLine("{0:X}",c);
Console.WriteLine("{0:n}",c);
Console.WriteLine("{0:C2}",c);
Console.WriteLine(c.ToString( "C2", CultureInfo.CreateSpecificCulture("en-US")));
Console.WriteLine(c.ToString( "n", CultureInfo.CreateSpecificCulture("pl-PL")));
Console.WriteLine(c.ToString( "n0",CultureInfo.InvariantCulture));
// Ustawienia regionalne PL

Console.WriteLine(String.Format(CultureInfo.InvariantCulture,"{0:0.000}", d));

int liczba = 123;
float fliczba = liczba;
Console.WriteLine(fliczba);
Console.WriteLine(typeof(fliczba));