using System.Globalization;
using System.Net.NetworkInformation;



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


// Console.WriteLine("{0} {1} {2} {3} {4} {5} {6}, {7}",a,b,c,c1,c2,d,e,s);
Console.WriteLine($"{a} {b} {c} {c1} {c2} {d} {e} {s}");



Console.WriteLine(String.Format(CultureInfo.InvariantCulture,"{0:0.000}", d));

double pi = Math.PI;
double r = 123;
Console.Write("Podaj promień koła:  ");
r = Convert.ToDouble(Console.ReadLine());

int pole = Convert.ToInt32(2*pi*r);

Console.WriteLine($"Obwód koła o promieniu {r} wynosi: {pole}");

var x = 3;
// x = 3.5;

Console.WriteLine(x);




