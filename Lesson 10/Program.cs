using Fraction;
using Point;
class App
{
      
    static void Main()
    {
        CFraction c = new ();
        CFraction d = new (1,-2);
        CFraction e;
        
        c.Numerator = 5;
        c.Denominator = 0;
        e = c * d;
        // e++;
        Console.WriteLine($"{c}, {d}, {e}");


        CPoint A = new();
        A.X = 23;
        A.Y = 45;
        CPoint3D B = new();
        B.X = 12;
        B.Y = 34;
        B.Z = 56;
        Console.WriteLine($"{A} {B}");
    }

}