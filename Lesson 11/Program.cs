using Fraction;
using Point;
using StringExtensions;






class App
{
    static void test()
    {
        // CPoint A = new();
        //     A.X = 23;
        //     A.Y = 45;
            CPoint3D B;
            B = new CPoint3D();
            B = null;
            // B.X = 12;
            // B.Y = 34;
            // B.Z = 56;
            // Console.WriteLine($"{A} {B}");
            // B=new CPoint3D();
            // B.X = A.X;
            // Console.WriteLine($"{B}");
    }

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

        for(int i=0;i<100;i++)
        {
            test();  
        }
        GC.Collect();



        string PrzykladowyTekst = "ala ma kota";
        Console.WriteLine(PrzykladowyTekst.Capitalize());
        Console.WriteLine(PrzykladowyTekst.Title());
    
    }

}

